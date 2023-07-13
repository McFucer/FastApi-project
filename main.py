from fastapi import FastAPI

app = FastAPI()

@app.get('/api/{name}/{age}')
async def get_ibninfo(name: str,
                     age: int):
    return {'name':name,
            'age':age}
@app.get('/api/{id}')
async def get_id(id:int):
    return {'ID': id}

db = []

@app.post('/api/')
async def post(name: str,
               last_name : str):
    db = {'name':name,
          'last_name':last_name}
    print(db)
    return {'name':name,
          'last_name':last_name}

db_ns = []

@app.post('/api/{name}/{l_name}')
async def NS(name: str,
             l_name: str):
    db_ns = {'name':name.lower(),
          'last_name':l_name.lower()}
    print(db_ns)
    return {'name':name.lower(),
          'last_name ':l_name.lower()}
