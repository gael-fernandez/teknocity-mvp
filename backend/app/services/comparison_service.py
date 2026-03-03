from sqlalchemy.orm import Session
from app.models.experiment import Experiment


def compare_latest_experiments(db: Session):
    experiments = (
        db.query(Experiment)
        .order_by(Experiment.created_at.desc())
        .limit(2)
        .all()
    )

    # 🔎 Caso 1: Base vacía
    if len(experiments) == 0:
        return {"message": "No experiments found"}

    # 🔎 Caso 2: Solo uno
    if len(experiments) == 1:
        return {"message": "Not enough experiments to compare"}

    exp1, exp2 = experiments

    strategies = {exp1.strategy, exp2.strategy}

    # 🔎 Caso 3: No es baseline + rl
    if "baseline" not in strategies or "rl" not in strategies:
        return {
            "message": "Latest experiments are not a baseline and rl pair"
        }

    baseline = exp1 if exp1.strategy == "baseline" else exp2
    rl = exp1 if exp1.strategy == "rl" else exp2

    # 🛡 Protección contra división por cero
    if baseline.average_wait_time == 0 or baseline.throughput == 0:
        return {
            "message": "Invalid baseline metrics for comparison"
        }

    wait_time_reduction = (
        (baseline.average_wait_time - rl.average_wait_time)
        / baseline.average_wait_time
    ) * 100

    throughput_increase = (
        (rl.throughput - baseline.throughput)
        / baseline.throughput
    ) * 100

    return {
        "baseline_id": baseline.id,
        "rl_id": rl.id,
        "baseline": {
            "average_wait_time": baseline.average_wait_time,
            "throughput": baseline.throughput,
        },
        "rl": {
            "average_wait_time": rl.average_wait_time,
            "throughput": rl.throughput,
        },
        "comparison": {
            "wait_time_reduction_percent": round(wait_time_reduction, 2),
            "throughput_increase_percent": round(throughput_increase, 2),
        },
    }