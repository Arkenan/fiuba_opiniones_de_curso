class ExcepcionNoHayDatos(Exception):
    def __init__(self, periodo):
        self.anio = periodo.anio
        self.cuatrimestre = periodo.cuatrimestre
        self.message = "No hay datos para el año %d, cuatrimestre %d" % (
            self.anio,
            self.cuatrimestre,
        )
