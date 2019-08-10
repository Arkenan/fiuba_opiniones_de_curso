import pytest
import csv
from numpy import NaN
from numpy import isnan
from modelo.dificultad import Dificultad

def test_numerico():
    assert Dificultad('Muy Difícil').puntos == 5
    assert Dificultad('Difícil').puntos == 4
    assert Dificultad('Normal').puntos == 3
    assert Dificultad('Fácil').puntos == 2
    assert Dificultad('Muy Fácil').puntos == 1
    assert isnan(Dificultad('No hay TP').puntos)
