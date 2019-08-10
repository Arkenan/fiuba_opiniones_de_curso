import pytest
import csv
from app.opiniones_parser import OpinionesParser

def test_should_fail_if_file_not_found():
    with pytest.raises(FileNotFoundError):
        parser = OpinionesParser('archivo_falso.csv')

def test_materia_y_curso_separados_guion():
    parser = OpinionesParser('tests/archivo_guion.csv')
    opinion = parser.next()
    assert opinion.asignatura == 'Análisis Numérico'
    assert opinion.curso == 'Schwarz'

def test_aprobo():
    parser = OpinionesParser('tests/archivo_guion.csv')
    opinion = parser.next()
    assert opinion.aprobo
