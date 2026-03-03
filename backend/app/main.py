from fastapi import FastAPI
from app.db.session import engine, Base
from app.services.simulation_service import get_all_experiments
from app.models import experiment  # importa el modelo
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.simulation_service import run_simulation
app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/status")
def status():
    return {"status": "ok"}
@app.post("/simulate")
def simulate(db: Session = Depends(get_db)):
    return run_simulation(db)
@app.get("/experiments")
def list_experiments(db: Session = Depends(get_db)):
    return get_all_experiments(db)

from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.comparison_service import compare_latest_experiments


@app.get("/compare")
def compare(db: Session = Depends(get_db)):
    return compare_latest_experiments(db)