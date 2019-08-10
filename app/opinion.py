from app.interes import Interes
from app.general import OpinionGeneral

class Opinion:
    def __init__(self, asignatura = "", curso = "", aprobo = False, interes = Interes('Interesantes'), general = OpinionGeneral('Bueno')):
        self.asignatura = asignatura
        self.curso = curso
        self.aprobo = aprobo
        self.interes = interes
        self.general = general
