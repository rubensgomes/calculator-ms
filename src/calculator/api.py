from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .calculator import Calculator

app = FastAPI()
calc = Calculator()


class OperationRequest(BaseModel):
    a: float
    b: float


class SingleOperandRequest(BaseModel):
    a: float


class RoundRequest(BaseModel):
    a: float
    decimals: int = 0


class OperationResponse(BaseModel):
    result: float


# Core Arithmetic


@app.post("/add", response_model=OperationResponse)
def add(req: OperationRequest):
    return OperationResponse(result=calc.add(req.a, req.b))


@app.post("/subtract", response_model=OperationResponse)
def subtract(req: OperationRequest):
    return OperationResponse(result=calc.subtract(req.a, req.b))


@app.post("/multiply", response_model=OperationResponse)
def multiply(req: OperationRequest):
    return OperationResponse(result=calc.multiply(req.a, req.b))


@app.post("/divide", response_model=OperationResponse)
def divide(req: OperationRequest):
    try:
        result = calc.divide(req.a, req.b)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return OperationResponse(result=result)


# Power & Roots


@app.post("/power", response_model=OperationResponse)
def power(req: OperationRequest):
    return OperationResponse(result=calc.power(req.a, req.b))


@app.post("/sqrt", response_model=OperationResponse)
def sqrt(req: SingleOperandRequest):
    try:
        result = calc.sqrt(req.a)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return OperationResponse(result=result)


@app.post("/nth_root", response_model=OperationResponse)
def nth_root(req: OperationRequest):
    try:
        result = calc.nth_root(req.a, req.b)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return OperationResponse(result=result)


# Modulo & Integer Math


@app.post("/modulo", response_model=OperationResponse)
def modulo(req: OperationRequest):
    try:
        result = calc.modulo(req.a, req.b)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return OperationResponse(result=result)


@app.post("/floor_divide", response_model=OperationResponse)
def floor_divide(req: OperationRequest):
    try:
        result = calc.floor_divide(req.a, req.b)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return OperationResponse(result=result)


# Absolute & Rounding


@app.post("/absolute", response_model=OperationResponse)
def absolute(req: SingleOperandRequest):
    return OperationResponse(result=calc.absolute(req.a))


@app.post("/round", response_model=OperationResponse)
def round_number(req: RoundRequest):
    return OperationResponse(result=calc.round_number(req.a, req.decimals))


@app.post("/floor", response_model=OperationResponse)
def floor(req: SingleOperandRequest):
    return OperationResponse(result=calc.floor(req.a))


@app.post("/ceil", response_model=OperationResponse)
def ceil(req: SingleOperandRequest):
    return OperationResponse(result=calc.ceil(req.a))


# Logarithmic & Exponential


@app.post("/log10", response_model=OperationResponse)
def log10(req: SingleOperandRequest):
    try:
        result = calc.log10(req.a)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return OperationResponse(result=result)


@app.post("/ln", response_model=OperationResponse)
def ln(req: SingleOperandRequest):
    try:
        result = calc.ln(req.a)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return OperationResponse(result=result)


@app.post("/exp", response_model=OperationResponse)
def exp(req: SingleOperandRequest):
    return OperationResponse(result=calc.exp(req.a))
