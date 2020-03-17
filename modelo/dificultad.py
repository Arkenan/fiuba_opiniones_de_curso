from numpy import NaN
from unidecode import unidecode


class Dificultad:
    MAP = {
        "muy dificil": 5,
        "dificil": 4,
        "normal": 3,
        "facil": 2,
        "muy facil": 1,
        "no hay tp": NaN,
    }

    def __init__(self, texto_dificultad):
        self.texto = texto_dificultad
        self.puntos = self.MAP[unidecode(texto_dificultad.lower())]
