from app.interes import Interes
from app.general import OpinionGeneral
from app.nivel_clases import NivelClases

class Opinion:
    def __init__(self, asignatura = "", curso = "", aprobo = False,
                 interes = Interes('Interesantes'),
                 general = OpinionGeneral('Bueno'), actual = False,
                 nivel_teoricas = NivelClases('Buenas'),
                 nivel_practicas = NivelClases('Buenas')):
        self.asignatura = asignatura
        self.curso = curso
        self.aprobo = aprobo
        self.interes = interes
        self.general = general
        self.actual = actual
        self.nivel_teoricas = nivel_teoricas
        self.nivel_practicas = nivel_practicas
