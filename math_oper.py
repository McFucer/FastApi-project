from fastapi import FastAPI

app = FastAPI()

@app.get('/api/{oper}/{num1}/{num2}')
async def oper(num1: int,
               oper:str,
               num2:int):
    if oper == '+':
        result = num1 + num2
        return result
    elif oper == '-':
        result = num1 - num2
        return result
    elif oper == '*':
        result = num1 * num2
        return result
    elif oper == '/':
        result = num1 / num2
        return result

@app.get('/api/{money}/{percent}')
async def oper(money: int,
               percent: int):
    result4minus = money*(percent/100)
    result = money - result4minus
    return result
