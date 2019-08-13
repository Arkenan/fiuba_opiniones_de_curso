class Curso:
    def __init__(self, nombre, ):
        self.nombre = nombre
        self.opiniones = []

    def add(self, opinion):
        self.opiniones.append(opinion)

    def __iter__(self):
        self.iterador = iter(self.opiniones)
        return self

    def __next__(self):
        return next(self.iterador)
