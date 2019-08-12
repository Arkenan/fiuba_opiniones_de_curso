from app.excepcion_cuatrimestre_no_valido import ExcepcionCuatrimestreNoValido

class Periodo:
    def __init__(self, anio, cuatrimestre):
        if cuatrimestre not in [1, 2]:
            raise ExcepcionCuatrimestreNoValido(cuatrimestre)
        self.anio = anio
        self.cuatrimestre = cuatrimestre
