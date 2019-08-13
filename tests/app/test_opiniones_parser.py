import pytest
import csv
from app.opiniones_parser import OpinionesParser

def test_should_fail_if_file_not_found():
    with pytest.raises(FileNotFoundError):
        parser = OpinionesParser('archivo_falso.csv')

def test_materia_y_curso_separados_guion():
    opinion = OpinionesParser('tests/app/encuesta.csv').next()
    assert opinion.asignatura == 'Análisis Numérico'
    assert opinion.curso == 'Schwarz'

def test_materia_y_curso_separados_coma():
    parser = OpinionesParser('tests/app/encuesta.csv')
    parser.next()
    opinion = parser.next()
    assert opinion.asignatura == 'Algoritmos y Programación I'
    assert opinion.curso == 'Costa'

def test_materia_y_curso_guien_sin_espacio():
    opinion = OpinionesParser('tests/app/encuesta_guion_sin_espacio.csv').next()
    assert opinion.asignatura == 'Computación'
    assert opinion.curso == 'Calvo'

def test_aprobo():
    opinion = OpinionesParser('tests/app/encuesta.csv').next()
    assert opinion.aprobo

def test_interes():
    opinion = OpinionesParser('tests/app/encuesta.csv').next()
    assert opinion.interes.puntos == 4
    assert opinion.interes.texto == 'Muy Interesantes'

def test_opinion_general():
    opinion = OpinionesParser('tests/app/encuesta.csv').next()
    assert opinion.general.puntos == 5
    assert opinion.general.texto == "Excelente"

def test_actual():
    opinion = OpinionesParser('tests/app/encuesta.csv').next()
    assert opinion.actual

def test_nivel_clases():
    opinion = OpinionesParser('tests/app/encuesta.csv').next()
    assert opinion.nivel_teoricas.puntos == 3
    assert opinion.nivel_practicas.puntos == 5

def test_dificultad():
    opinion = OpinionesParser('tests/app/encuesta.csv').next()
    assert opinion.dificultad_curso.puntos == 4
    assert opinion.dificultad_tp.puntos == 3

def test_texto():
    parser = OpinionesParser('tests/app/encuesta.csv')
    opinion = parser.next()
    assert 'Creo que' in opinion.texto
    opinion = parser.next()
    assert opinion.texto == ''

# No falla leer las opiniones del 2019-1C.
def test_2019_1C():
    parser = OpinionesParser('data/encuesta-dc-2019-1C.csv')
    [opinion for opinion in parser]
