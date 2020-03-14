from modelo.excepcion_cuatrimestre_no_valido import ExcepcionCuatrimestreNoValido

class Periodo:
    def __init__(self, anio, cuatrimestre):
        if cuatrimestre not in [1, 2]:
            raise ExcepcionCuatrimestreNoValido(cuatrimestre)
        self.anio = anio
        self.cuatrimestre = cuatrimestre

    def __str__(self):
        return '%d - %d%s Cuatrimestre' % (self.anio, self.cuatrimestre, self._sufijo())

    def _sufijo(self):
        return 'do' if self.cuatrimestre == 2 else 'er'
