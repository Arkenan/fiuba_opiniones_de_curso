class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []

    def add(self, curso):
        self.cursos.append(curso)

    def __iter__(self):
        self.iterador = iter(self.cursos)
        return self

    def __next__(self):
        return next(self.iterador)
