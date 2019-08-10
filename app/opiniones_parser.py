import csv
from app.opinion import Opinion

class OpinionesParser:
    def __init__(self, nombre_archivo):
        self.csv = csv.DictReader(open(nombre_archivo), delimiter = ',')

    def next(self):
        csv_opinion = next(self.csv)
        asignatura, curso = self.get_curso(csv_opinion)
        aprobo = self.aprobo(csv_opinion)
        return Opinion(asignatura = asignatura, curso = curso, aprobo = aprobo)

    def get_curso(self, csv_opinion):
        # TODO check invalida.
        asignatura, curso = csv_opinion['Elige el curso'].split('-')
        return asignatura[:-1], curso[1:]

    def aprobo(self, csv_opinion):
        return csv_opinion['¿Aprobó la Cursada?'].lower() == 'sí'
