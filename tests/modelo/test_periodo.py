from modelo.periodo import Periodo
from modelo.excepcion_cuatrimestre_no_valido import ExcepcionCuatrimestreNoValido
import unittest

class OpinionesRepoTestCase(unittest.TestCase):
    def test_valido(self):
        periodo = Periodo(2019, 1)
        assert periodo.anio == 2019
        assert periodo.cuatrimestre == 1

    def test_no_valido(self):
        with self.assertRaises(ExcepcionCuatrimestreNoValido):
            Periodo(1900, 3)
