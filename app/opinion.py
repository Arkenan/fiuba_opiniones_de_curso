from app.interes import Interes

class Opinion:
    def __init__(self, asignatura = "", curso = "", aprobo = False, interes = Interes('Interesantes')):
        self.asignatura = asignatura
        self.curso = curso
        self.aprobo = aprobo
        self.interes = interes
