class ExcepcionNoHayDatos(Exception):
    def __init__(self, anio, cuatrimestre):
        self.anio = anio
        self.cuatrimestre = cuatrimestre
        self.message = "No hay datos para el año %d, cuatrimestre %d" % (anio, cuatrimestre)
