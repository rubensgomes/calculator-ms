"""FastAPI REST endpoints for the calculator microservice.

Each endpoint accepts a POST request with a JSON body, delegates to
:class:`calculator.calculator.Calculator`, and returns a JSON response
containing the result.
"""

import logging

import yaml
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, Response
from pydantic import BaseModel

from .calculator import Calculator
from .config import load_config, setup_logging

load_config()
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Calculator Microservice",
    description="Arithmetic operations via REST API.\n\n"
    "Download the [OpenAPI 3.1 spec (YAML)](/openapi.yaml).",
)
calc = Calculator()


@app.get("/", include_in_schema=False)
def root():
    """Redirect the landing page to Swagger UI."""
    return RedirectResponse(url="/docs")


@app.get("/openapi.yaml", include_in_schema=False)
def openapi_yaml():
    """Return the OpenAPI 3.1 spec as YAML."""
    openapi_schema = app.openapi()
    yaml_content = yaml.dump(openapi_schema, sort_keys=False, allow_unicode=True)
    return Response(
        content=yaml_content, media_type="application/vnd.oai.openapi;version=3.1"
    )


class OperationRequest(BaseModel):
    """Request body for two-operand operations."""

    a: float
    b: float


class SingleOperandRequest(BaseModel):
    """Request body for single-operand operations."""

    a: float


class RoundRequest(BaseModel):
    """Request body for the rounding operation."""

    a: float
    decimals: int = 0


class OperationResponse(BaseModel):
    """Standard response body containing a single float result."""

    result: float


# Core Arithmetic


@app.post("/add", response_model=OperationResponse)
def add(req: OperationRequest):
    """Return the sum of two numbers."""
    logger.debug("POST /add: a=%s, b=%s", req.a, req.b)
    result = calc.add(req.a, req.b)
    logger.info("add(%s, %s) = %s", req.a, req.b, result)
    return OperationResponse(result=result)


@app.post("/subtract", response_model=OperationResponse)
def subtract(req: OperationRequest):
    """Return the difference of two numbers."""
    logger.debug("POST /subtract: a=%s, b=%s", req.a, req.b)
    result = calc.subtract(req.a, req.b)
    logger.info("subtract(%s, %s) = %s", req.a, req.b, result)
    return OperationResponse(result=result)


@app.post("/multiply", response_model=OperationResponse)
def multiply(req: OperationRequest):
    """Return the product of two numbers."""
    logger.debug("POST /multiply: a=%s, b=%s", req.a, req.b)
    result = calc.multiply(req.a, req.b)
    logger.info("multiply(%s, %s) = %s", req.a, req.b, result)
    return OperationResponse(result=result)


@app.post("/divide", response_model=OperationResponse)
def divide(req: OperationRequest):
    """Return the quotient of two numbers.

    Returns an HTTP 400 Bad Request error on division by zero.
    """
    logger.debug("POST /divide: a=%s, b=%s", req.a, req.b)
    try:
        result = calc.divide(req.a, req.b)
    except ValueError as e:
        logger.warning("Validation error on /divide: %s", e)
        raise HTTPException(status_code=400, detail=str(e)) from e
    logger.info("divide(%s, %s) = %s", req.a, req.b, result)
    return OperationResponse(result=result)


# Power & Roots


@app.post("/power", response_model=OperationResponse)
def power(req: OperationRequest):
    """Return a raised to the power b."""
    logger.debug("POST /power: a=%s, b=%s", req.a, req.b)
    result = calc.power(req.a, req.b)
    logger.info("power(%s, %s) = %s", req.a, req.b, result)
    return OperationResponse(result=result)


@app.post("/sqrt", response_model=OperationResponse)
def sqrt(req: SingleOperandRequest):
    """Return the square root. Returns an HTTP 400 Bad Request error on negative input."""
    logger.debug("POST /sqrt: a=%s", req.a)
    try:
        result = calc.sqrt(req.a)
    except ValueError as e:
        logger.warning("Validation error on /sqrt: %s", e)
        raise HTTPException(status_code=400, detail=str(e)) from e
    logger.info("sqrt(%s) = %s", req.a, result)
    return OperationResponse(result=result)


@app.post("/nth_root", response_model=OperationResponse)
def nth_root(req: OperationRequest):
    """Return the b-th root of a. Returns an HTTP 400 Bad Request error on invalid input."""
    logger.debug("POST /nth_root: a=%s, b=%s", req.a, req.b)
    try:
        result = calc.nth_root(req.a, req.b)
    except ValueError as e:
        logger.warning("Validation error on /nth_root: %s", e)
        raise HTTPException(status_code=400, detail=str(e)) from e
    logger.info("nth_root(%s, %s) = %s", req.a, req.b, result)
    return OperationResponse(result=result)


# Modulo & Integer Math


@app.post("/modulo", response_model=OperationResponse)
def modulo(req: OperationRequest):
    """Return a mod b. Returns an HTTP 400 Bad Request error on modulo by zero."""
    logger.debug("POST /modulo: a=%s, b=%s", req.a, req.b)
    try:
        result = calc.modulo(req.a, req.b)
    except ValueError as e:
        logger.warning("Validation error on /modulo: %s", e)
        raise HTTPException(status_code=400, detail=str(e)) from e
    logger.info("modulo(%s, %s) = %s", req.a, req.b, result)
    return OperationResponse(result=result)


@app.post("/floor_divide", response_model=OperationResponse)
def floor_divide(req: OperationRequest):
    """Return the floor division of a by b.

    Returns an HTTP 400 Bad Request error on division by zero.
    """
    logger.debug("POST /floor_divide: a=%s, b=%s", req.a, req.b)
    try:
        result = calc.floor_divide(req.a, req.b)
    except ValueError as e:
        logger.warning("Validation error on /floor_divide: %s", e)
        raise HTTPException(status_code=400, detail=str(e)) from e
    logger.info("floor_divide(%s, %s) = %s", req.a, req.b, result)
    return OperationResponse(result=result)


# Absolute & Rounding


@app.post("/absolute", response_model=OperationResponse)
def absolute(req: SingleOperandRequest):
    """Return the absolute value."""
    logger.debug("POST /absolute: a=%s", req.a)
    result = calc.absolute(req.a)
    logger.info("absolute(%s) = %s", req.a, result)
    return OperationResponse(result=result)


@app.post("/round", response_model=OperationResponse)
def round_number(req: RoundRequest):
    """Return a rounded to the given number of decimal places."""
    logger.debug("POST /round: a=%s, decimals=%s", req.a, req.decimals)
    result = calc.round_number(req.a, req.decimals)
    logger.info("round(%s, %s) = %s", req.a, req.decimals, result)
    return OperationResponse(result=result)


@app.post("/floor", response_model=OperationResponse)
def floor(req: SingleOperandRequest):
    """Return the floor of a."""
    logger.debug("POST /floor: a=%s", req.a)
    result = calc.floor(req.a)
    logger.info("floor(%s) = %s", req.a, result)
    return OperationResponse(result=result)


@app.post("/ceil", response_model=OperationResponse)
def ceil(req: SingleOperandRequest):
    """Return the ceiling of a."""
    logger.debug("POST /ceil: a=%s", req.a)
    result = calc.ceil(req.a)
    logger.info("ceil(%s) = %s", req.a, result)
    return OperationResponse(result=result)


# Logarithmic & Exponential


@app.post("/log10", response_model=OperationResponse)
def log10(req: SingleOperandRequest):
    """Return the base-10 logarithm. Returns an HTTP 400 Bad Request error on non-positive input."""
    logger.debug("POST /log10: a=%s", req.a)
    try:
        result = calc.log10(req.a)
    except ValueError as e:
        logger.warning("Validation error on /log10: %s", e)
        raise HTTPException(status_code=400, detail=str(e)) from e
    logger.info("log10(%s) = %s", req.a, result)
    return OperationResponse(result=result)


@app.post("/ln", response_model=OperationResponse)
def ln(req: SingleOperandRequest):
    """Return the natural logarithm. Returns an HTTP 400 Bad Request error on non-positive input."""
    logger.debug("POST /ln: a=%s", req.a)
    try:
        result = calc.ln(req.a)
    except ValueError as e:
        logger.warning("Validation error on /ln: %s", e)
        raise HTTPException(status_code=400, detail=str(e)) from e
    logger.info("ln(%s) = %s", req.a, result)
    return OperationResponse(result=result)


@app.post("/exp", response_model=OperationResponse)
def exp(req: SingleOperandRequest):
    """Return e raised to the power a."""
    logger.debug("POST /exp: a=%s", req.a)
    result = calc.exp(req.a)
    logger.info("exp(%s) = %s", req.a, result)
    return OperationResponse(result=result)
