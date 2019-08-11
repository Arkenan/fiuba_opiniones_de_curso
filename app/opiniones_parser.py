import csv
from modelo.opinion import Opinion
from modelo.interes import Interes
from modelo.general import OpinionGeneral
from modelo.nivel_clases import NivelClases
from modelo.dificultad import Dificultad
from app.excepcion_curso_no_valido import ExcepcionCursoNoValido

class OpinionesParser:
    TEXTO = 'Comentarios Sobre el Curso'

    def __init__(self, nombre_archivo):
        self.csv = csv.DictReader(open(nombre_archivo), delimiter = ',')

    def next(self):
        csv_opinion = next(self.csv)
        asignatura, curso = self.get_curso(csv_opinion)
        return Opinion(
            asignatura = asignatura, curso = curso,
            aprobo = self.aprobo(csv_opinion),
            interes = self.interes(csv_opinion),
            general = self.general(csv_opinion),
            actual = self.actual(csv_opinion),
            nivel_teoricas = self.nivel_teoricas(csv_opinion),
            nivel_practicas = self.nivel_practicas(csv_opinion),
            dificultad_curso = self.dificultad_curso(csv_opinion),
            dificultad_tp = self.dificultad_tp(csv_opinion),
            texto = csv_opinion[self.TEXTO])

    def get_curso(self, csv_opinion):
        # TODO check invalida.
        curso_csv = csv_opinion['Elige el curso']
        if '-' in curso_csv:
            asignatura, curso = curso_csv.split('-')
            return asignatura[:-1], curso[1:]
        elif ',' in curso_csv:
            asignatura, curso = curso_csv.split(',')
            return asignatura, curso[1:]
        raise ExcepcionCursoNoValido(csv_opinion['Elige el curso'])

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

    def dificultad_curso(self, csv_opinion):
        return Dificultad(csv_opinion['Dificultad del Curso'])

    def dificultad_tp(self, csv_opinion):
        return Dificultad(csv_opinion['Dificultad del TP'])

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()
