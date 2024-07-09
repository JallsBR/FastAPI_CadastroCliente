from pydantic import BaseModel

class Cliente(BaseModel):
    nome: str
    celular: str
    email: str
    nascimento: str
    endereco: str
    genero: str
    porfissao: str






