import pytest
import csv
from app.opiniones_parser import OpinionesParser

def test_should_fail_if_file_not_found():
    with pytest.raises(FileNotFoundError):
        parser = OpinionesParser('archivo_falso.csv')

def test_materia_y_curso_separados_guion():
    opinion = OpinionesParser('tests/archivo_guion.csv').next()
    assert opinion.asignatura == 'Análisis Numérico'
    assert opinion.curso == 'Schwarz'

def test_aprobo():
    opinion = OpinionesParser('tests/archivo_guion.csv').next()
    assert opinion.aprobo

def test_interes():
    opinion = OpinionesParser('tests/archivo_guion.csv').next()
    assert opinion.interes.puntos == 4
    assert opinion.interes.texto == 'Muy Interesantes'

def test_opinion_general():
    opinion = OpinionesParser('tests/archivo_guion.csv').next()
    assert opinion.general.puntos == 5
    assert opinion.general.texto == "Excelente"

def test_actual():
    opinion = OpinionesParser('tests/archivo_guion.csv').next()
    assert opinion.actual

def test_nivel_clases():
    opinion = OpinionesParser('tests/archivo_guion.csv').next()
    assert opinion.nivel_teoricas.puntos == 3
    assert opinion.nivel_practicas.puntos == 5

def test_dificultad():
    opinion = OpinionesParser('tests/archivo_guion.csv').next()
    assert opinion.dificultad_curso.puntos == 4
    assert opinion.dificultad_tp.puntos == 3
