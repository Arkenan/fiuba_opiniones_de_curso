import csv
from app.opinion import Opinion
from app.interes import Interes
from app.general import OpinionGeneral
from app.nivel_clases import NivelClases

class OpinionesParser:
    def __init__(self, nombre_archivo):
        self.csv = csv.DictReader(open(nombre_archivo), delimiter = ',')

    def next(self):
        csv_opinion = next(self.csv)
        asignatura, curso = self.get_curso(csv_opinion)
        aprobo = self.aprobo(csv_opinion)
        interes = self.interes(csv_opinion)
        general = self.general(csv_opinion)
        actual = self.actual(csv_opinion)
        nivel_teoricas = self.nivel_teoricas(csv_opinion)
        nivel_practicas = self.nivel_practicas(csv_opinion)
        return Opinion(
            asignatura = asignatura, curso = curso, aprobo = aprobo,
            interes = interes, general = general, actual = actual,
            nivel_teoricas = nivel_teoricas, nivel_practicas = nivel_practicas)

    def get_curso(self, csv_opinion):
        # TODO check invalida.
        asignatura, curso = csv_opinion['Elige el curso'].split('-')
        return asignatura[:-1], curso[1:]

    def aprobo(self, csv_opinion):
        return csv_opinion['¿Aprobó la Cursada?'].lower() == 'sí'

    def actual(self, csv_opinion):
        return csv_opinion['¿Los Temas de la Materia Están Actualizados?'].lower() == 'sí'

    def interes(self, csv_opinion):
        return Interes(csv_opinion['¿Cómo te Resultaron los Temas de la Materia?'])

    def general(self, csv_opinion):
        return OpinionGeneral(csv_opinion['Opinión General Sobre el Curso'])

    def nivel_teoricas(self, csv_opinion):
        return NivelClases(csv_opinion['Nivel de las Clases Teóricas del Curso'])

    def nivel_practicas(self, csv_opinion):
        return NivelClases(csv_opinion['Nivel de las Clases Prácticas del Curso'])
