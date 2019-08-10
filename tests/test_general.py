import pytest
import csv
from app.interes import Interes
from app.general import OpinionGeneral

def test_numerico():
    assert OpinionGeneral('Excelente').puntos == 5
    assert OpinionGeneral('Muy Bueno').puntos == 4
    assert OpinionGeneral('Bueno').puntos == 3
    assert OpinionGeneral('Regular').puntos == 2
    assert OpinionGeneral('Malo').puntos == 1
