import pytest
from fastapi.testclient import TestClient

from calculator.api import app

client = TestClient(app)


def test_add():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_subtract():
    response = client.post("/subtract", json={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 6.0}


def test_multiply():
    response = client.post("/multiply", json={"a": 3, "b": 7})
    assert response.status_code == 200
    assert response.json() == {"result": 21.0}


def test_divide():
    response = client.post("/divide", json={"a": 15, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 3.75}


def test_divide_by_zero():
    response = client.post("/divide", json={"a": 1, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}


def test_power():
    response = client.post("/power", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8.0}


def test_modulo():
    response = client.post("/modulo", json={"a": 10, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 1.0}


def test_modulo_by_zero():
    response = client.post("/modulo", json={"a": 10, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot modulo by zero"}


def test_sqrt():
    response = client.post("/sqrt", json={"a": 16})
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}


def test_sqrt_negative():
    response = client.post("/sqrt", json={"a": -1})
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot take square root of a negative number"}


def test_nth_root():
    response = client.post("/nth_root", json={"a": 27, "b": 3})
    assert response.status_code == 200
    assert response.json()["result"] == pytest.approx(3.0)


def test_nth_root_zeroth():
    response = client.post("/nth_root", json={"a": 8, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot take zeroth root"}


def test_floor_divide():
    response = client.post("/floor_divide", json={"a": 7, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}


def test_floor_divide_by_zero():
    response = client.post("/floor_divide", json={"a": 7, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot floor divide by zero"}


def test_absolute():
    response = client.post("/absolute", json={"a": -5})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}


def test_round():
    response = client.post("/round", json={"a": 3.14159, "decimals": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3.14}


def test_round_default_decimals():
    response = client.post("/round", json={"a": 3.7})
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}


def test_floor():
    response = client.post("/floor", json={"a": 3.7})
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}


def test_ceil():
    response = client.post("/ceil", json={"a": 3.2})
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}


def test_log10():
    response = client.post("/log10", json={"a": 100})
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}


def test_log10_non_positive():
    response = client.post("/log10", json={"a": 0})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Cannot take logarithm of a non-positive number"
    }


def test_ln():
    response = client.post("/ln", json={"a": 1})
    assert response.status_code == 200
    assert response.json() == {"result": 0.0}


def test_ln_non_positive():
    response = client.post("/ln", json={"a": -1})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Cannot take logarithm of a non-positive number"
    }


def test_exp():
    response = client.post("/exp", json={"a": 0})
    assert response.status_code == 200
    assert response.json() == {"result": 1.0}
