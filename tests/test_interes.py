import pytest
import csv
from app.interes import Interes

def test_numerico():
    assert Interes('Muy Interesantes').puntos == 4
    assert Interes('Interesantes').puntos == 3
    assert Interes('Poco Interesantes').puntos == 2
    assert Interes('Nada Interesantes').puntos == 1
