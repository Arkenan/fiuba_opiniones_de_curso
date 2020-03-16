import unittest
from modelo.periodo import Periodo
from app.opiniones_repo import OpinionesRepo
from app.excepcion_no_hay_datos import ExcepcionNoHayDatos


class OpinionesRepoTestCase(unittest.TestCase):
    def test_archivo_correcto(self):
        opiniones = OpinionesRepo().opiniones_periodo(Periodo(2019, 1))
        assert len(opiniones) == 730
        assert opiniones[1].curso == "Schwarz"
        assert opiniones[-1].curso == "Kuhn"

    def test_no_hay_datos(self):
        with self.assertRaises(ExcepcionNoHayDatos) as context:
            OpinionesRepo().opiniones_periodo(Periodo(1900, 1))

        assert context.exception.anio == 1900
        assert context.exception.cuatrimestre == 1
