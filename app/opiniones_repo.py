from modelo.opinion import Opinion
from app.opiniones_parser import OpinionesParser

class OpinionesRepo:
    def opiniones_periodo(self, anio, cuatrimestre):
        parser = OpinionesParser('data/encuesta-dc-2019-1erC.csv')
        return [opinion for opinion in parser]
