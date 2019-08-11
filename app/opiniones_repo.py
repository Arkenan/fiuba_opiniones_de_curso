from modelo.opinion import Opinion
from app.opiniones_parser import OpinionesParser
from app.excepcion_no_hay_datos import ExcepcionNoHayDatos

class OpinionesRepo:
    def opiniones_periodo(self, anio, cuatrimestre):
        try:
            parser = OpinionesParser('data/encuesta-dc-%d-%dC.csv' % (anio, cuatrimestre))
            return [opinion for opinion in parser]
        except FileNotFoundError:
            raise ExcepcionNoHayDatos(anio, cuatrimestre)
