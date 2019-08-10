class ExcepcionCursoNoValido(Exception):
    def __init__(self, curso):
        self.message = curso
