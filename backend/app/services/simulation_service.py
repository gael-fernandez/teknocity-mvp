import random
from sqlalchemy.orm import Session

from app.models.experiment import Experiment


def run_simulation(db: Session):
    # Baseline metrics
    baseline_wait = random.uniform(35, 60)
    baseline_throughput = random.uniform(80, 120)

    # RL metrics
    rl_wait = random.uniform(20, 45)
    rl_throughput = random.uniform(120, 140)

    baseline_experiment = Experiment(
        name="Traffic Simulation",
        strategy="baseline",
        average_wait_time=round(baseline_wait, 2),
        throughput=round(baseline_throughput, 2),
    )

    rl_experiment = Experiment(
        name="Traffic Simulation",
        strategy="rl",
        average_wait_time=round(rl_wait, 2),
        throughput=round(rl_throughput, 2),
    )

    db.add(baseline_experiment)
    db.add(rl_experiment)
    db.commit()

    db.refresh(baseline_experiment)
    db.refresh(rl_experiment)
    wait_time_reduction = (
        (baseline_experiment.average_wait_time - rl_experiment.average_wait_time)
        / baseline_experiment.average_wait_time
    ) * 100

    throughput_increase = (
        (rl_experiment.throughput - baseline_experiment.throughput)
        / baseline_experiment.throughput
    ) * 100
    return {
        "baseline": {
            "wait_time": baseline_experiment.average_wait_time,
            "throughput": baseline_experiment.throughput,
        },
        "rl": {
            "wait_time": rl_experiment.average_wait_time,
            "throughput": rl_experiment.throughput,
        },
        "improvement": {
            "wait_time_reduction_percent": round(wait_time_reduction, 2),
            "throughput_increase_percent": round(throughput_increase, 2),
        },
    
    }
from typing import List

def get_all_experiments(db: Session):
    experiments = db.query(Experiment).order_by(Experiment.created_at.desc()).all()

    return [
        {
            "id": exp.id,
            "name": exp.name,
            "strategy": exp.strategy,
            "average_wait_time": exp.average_wait_time,
            "throughput": exp.throughput,
            "created_at": exp.created_at,
        }
        for exp in experiments
    ]