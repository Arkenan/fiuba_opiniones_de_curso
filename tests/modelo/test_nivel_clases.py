import pytest
import csv
from numpy import NaN
from numpy import isnan
from modelo.nivel_clases import NivelClases

def test_numerico():
    assert NivelClases('Excelentes').puntos == 5
    assert NivelClases('Muy Buenas').puntos == 4
    assert NivelClases('Buenas').puntos == 3
    assert NivelClases('Regulares').puntos == 2
    assert NivelClases('Malas').puntos == 1
    assert isnan(NivelClases('No hay clases teóricas').puntos)
    assert isnan(NivelClases('No hay Clases Prácticas').puntos)
