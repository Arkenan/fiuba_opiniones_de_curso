class ExcepcionCuatrimestreNoValido(Exception):
    def __init__(self, cuatrimestre):
        self.cuatrimestre = cuatrimestre
        self.message = "El cuatrimestre %d no es válido. Debe ser 1 o 2." % (cuatrimestre)
