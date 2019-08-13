from app.asignaturas_repo import AsignaturasRepo
from modelo.opinion import Opinion
import unittest

class AsignaturasRepoTestcase(unittest.TestCase):
    def test_generacion(self):
        opiniones = [
            Opinion(asignatura = 'b', curso = 'a'),
            Opinion(asignatura = 'a', curso = 'b'),
            Opinion(asignatura = 'a', curso = 'a'),
        ]

        asignaturas = AsignaturasRepo().generar_desde_opiniones(opiniones)
        assert asignaturas[0].nombre == 'a'
        cursos = [curso for curso in asignaturas[0]]
        assert len(cursos) == 2
        assert cursos[0].nombre == 'a'
        assert cursos[1].nombre == 'b'

        assert asignaturas[1].nombre == 'b'
        cursos = [curso for curso in asignaturas[1]]
        assert len(cursos) == 1
        assert cursos[0].nombre == 'a'
