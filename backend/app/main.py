from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
 
from app.db.session import engine, Base, get_db
from app.models import experiment
from app.services.simulation_service import run_simulation, get_all_experiments
from app.services.comparison_service import compare_latest_experiments
 
app = FastAPI(title="Teknocity API", version="1.0.0")
 
# ─── CORS — sin esto React no puede conectar ──────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite dev (frontend React)
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
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
 
@app.get("/compare")
def compare(db: Session = Depends(get_db)):
    return compare_latest_experiments(db)