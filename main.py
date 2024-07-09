from fastapi import FastAPI
from model.json_db import JsonDB
from model.cliente import Cliente


app = FastAPI()
clienteDB = JsonDB(path='./data/clientes.json')

@app.get('/cliente')
def get_clientes():
    cliente = clienteDB.read()
    return { "Return" :  cliente }

@app.post('/cliente')
def create_cliente(cliente: Cliente):
    clienteDB.insert_cliente(cliente)
    return {"status":"inserted"}

