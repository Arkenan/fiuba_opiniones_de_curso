from numpy import NaN


class Dificultad:
    MAP = {
        "muy difícil": 5,
        "difícil": 4,
        "normal": 3,
        "fácil": 2,
        "muy fácil": 1,
        "no hay tp": NaN,
    }

    def __init__(self, texto_interes):
        self.texto = texto_interes
        self.puntos = self.MAP[texto_interes.lower()]
