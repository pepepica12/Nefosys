from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Nefosys backend operativo"}

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"db": "Conexión exitosa a Neon"}
    except Exception as e:
        return {"db_error": str(e)}
