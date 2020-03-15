from modelo.asignatura import Asignatura
from modelo.curso import Curso


class AsignaturasRepo:
    # Genera una lista de asignaturas dada una lista de opiniones.
    def generar_desde_opiniones(self, opiniones):
        os = sorted(opiniones, key=lambda o: (o.asignatura, o.curso, o.general.puntos))
        asignaturas = []
        n = 0
        l = len(os)
        opinion = os[0]
        while n < l:
            asignatura = Asignatura(opinion.asignatura)
            while n < l and opinion.asignatura == asignatura.nombre:
                curso = Curso(opinion.curso)
                while (
                    n < l
                    and opinion.curso == curso.nombre
                    and opinion.asignatura == asignatura.nombre
                ):
                    curso.add(opinion)
                    n += 1
                    if n < l:
                        opinion = os[n]
                asignatura.add(curso)
            asignaturas.append(asignatura)
        return asignaturas
