from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:TugFe/23@localhost:5432/teknocity"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("Conexión exitosa a PostgreSQL 🚀")
    except Exception as e:
        print("Error de conexión:", e)