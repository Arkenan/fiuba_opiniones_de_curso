from modelo.periodo import Periodo
from modelo.excepcion_cuatrimestre_no_valido import ExcepcionCuatrimestreNoValido
import unittest

class PeriodoTestCase(unittest.TestCase):
    def test_valido(self):
        periodo = Periodo(2019, 1)
        assert periodo.anio == 2019
        assert periodo.cuatrimestre == 1

    def test_no_valido(self):
        with self.assertRaises(ExcepcionCuatrimestreNoValido):
            Periodo(1900, 3)

    def test_print_1(self):
        periodo = Periodo(1990, 1)
        assert periodo.__str__() == '1990 - 1er Cuatrimestre'

    def test_print_2(self):
        periodo = Periodo(1995, 2)
        assert periodo.__str__() == '1995 - 2do Cuatrimestre'
