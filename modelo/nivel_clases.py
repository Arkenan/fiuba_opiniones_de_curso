from numpy import NaN

class NivelClases:
    MAP = {'Excelentes':5,'Muy Buenas':4, 'Buenas':3,'Regulares':2,'Malas':1}

    def __init__(self, texto_interes):
        self.texto = texto_interes
        if 'No hay' in texto_interes:
            self.puntos = NaN
        else:
            self.puntos = self.MAP[texto_interes]
