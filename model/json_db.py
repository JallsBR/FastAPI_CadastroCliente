from pydantic import BaseModel
import json
from .cliente import Cliente

class JsonDB(BaseModel):
    path: str

    def read(self):
        f = open(self.path)
        data=json.loads(f.read())
        f.close()
        return data
    
    def insert_cliente(self, cliente:Cliente):
        data=self.read()
        data['clientes'].append(cliente.dict())
        f = open(self.path, 'w')
        f.write(json.dumps(data , indent=2, separators= (',', ': ')))
        f.close()
        return data
    