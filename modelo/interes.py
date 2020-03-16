class Interes:
    MAP = {
        "Nada Interesantes": 1,
        "Poco Interesantes": 2,
        "Interesantes": 3,
        "Muy Interesantes": 4,
    }

    def __init__(self, texto_interes):
        self.texto = texto_interes
        self.puntos = self.MAP[texto_interes]
