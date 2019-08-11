import unittest
from app.opiniones_repo import OpinionesRepo
from app.excepcion_no_hay_datos import ExcepcionNoHayDatos
from app.excepcion_cuatrimestre_no_valido import ExcepcionCuatrimestreNoValido

class OpinionesRepoTestCase(unittest.TestCase):
    def test_archivo_correcto(self):
        opiniones = OpinionesRepo().opiniones_periodo(2019, 1)
        assert len(opiniones) == 730
        assert opiniones[1].curso == 'Schwarz'
        assert opiniones[-1].curso == 'Kuhn'

    def test_no_hay_datos(self):
        with self.assertRaises(ExcepcionNoHayDatos) as context:
            OpinionesRepo().opiniones_periodo(1900, 1)

        assert context.exception.anio == 1900
        assert context.exception.cuatrimestre == 1

    def test_cuatrimestre_no_valido(self):
        with self.assertRaises(ExcepcionCuatrimestreNoValido) as context:
            OpinionesRepo().opiniones_periodo(1900, 3)

        assert context.exception.cuatrimestre == 3
