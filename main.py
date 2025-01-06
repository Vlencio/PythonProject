from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import cadastro
from cadastro import get_db
from databases import engine
from models import Base

app = FastAPI()

@app.get('/')
def test():
    return {'message': 'Mensagem'}

class NewUser(BaseModel):
    name: str
    email: str
    password: str

@app.post('/new_user')
def create_user(payload: NewUser, db: Session = Depends(get_db)):
    retorno = cadastro.create_user(payload.name, payload.email, payload.password, db)
    return retorno

@app.get('/new_user/{email}')
def search_email(email: str, db: Session = Depends(get_db)):
    user = cadastro.search(email, db)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado.")
    return {'id': user.id, 'email': user.email, 'name': user.name}




Base.metadata.create_all(bind=engine)