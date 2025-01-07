import cadastro, login
from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from cadastro import get_db
from databases import engine
from models import Base
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou substitua "*" por uma lista de URLs específicas permitidas
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

@app.get('/')
def test():
    return {'message': 'Teste'}

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
    return {'id': user.id, 'email': user.email, 'senha': user.password}

class LoginRequest(BaseModel):
    email: str
    password: str

@app.post('/login')
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    retorno = cadastro.login(payload.email, payload.password, db)
    if retorno is not None:
        return {'message': 'Login Bem Sucedido.'}
    else:
        raise HTTPException(status_code=401, detail='Credenciais invalidas.')

Base.metadata.create_all(bind=engine)