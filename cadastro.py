from fastapi.params import Depends
from sqlalchemy.orm import Session
from databases import SessionLocal
from models import User

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(name, email, password,db: Session):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return {"error": "Email já registrado."}

    new_user = User(
        name = name,
        email = email,
        password = password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, 'name': new_user.name, 'email': new_user.email}

def search(email: str, db: Session):
    return db.query(User).filter(User.email == email).first()