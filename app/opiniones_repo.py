from modelo.opinion import Opinion
from app.opiniones_parser import OpinionesParser
from app.excepcion_no_hay_datos import ExcepcionNoHayDatos
from app.excepcion_cuatrimestre_no_valido import ExcepcionCuatrimestreNoValido

class OpinionesRepo:
    def opiniones_periodo(self, anio, cuatrimestre):
        if cuatrimestre not in [1, 2]:
            raise ExcepcionCuatrimestreNoValido(cuatrimestre)
        try:
            parser = OpinionesParser('data/encuesta-dc-%d-%dC.csv' % (anio, cuatrimestre))
            return [opinion for opinion in parser]
        except FileNotFoundError:
            raise ExcepcionNoHayDatos(anio, cuatrimestre)
