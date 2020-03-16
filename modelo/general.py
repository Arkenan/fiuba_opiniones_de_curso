class OpinionGeneral:
    MAP = {"Excelente": 5, "Muy Bueno": 4, "Bueno": 3, "Regular": 2, "Malo": 1}

    def __init__(self, texto_interes):
        self.texto = texto_interes
        self.puntos = self.MAP[texto_interes]
