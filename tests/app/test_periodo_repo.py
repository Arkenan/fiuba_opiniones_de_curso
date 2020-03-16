from app.periodo_repo import PeriodoRepo


def test_presente_2019_1C():
    periodos = PeriodoRepo().get_all()
    encontrado = False
    for periodo in periodos:
        if periodo.anio == 2019 and periodo.cuatrimestre == 1:
            encontrado = True
    assert encontrado
