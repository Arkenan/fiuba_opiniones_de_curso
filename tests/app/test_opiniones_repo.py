from app.opiniones_repo import OpinionesRepo

def test_archivo_correcto():
    opiniones = OpinionesRepo().opiniones_periodo(2019, 1)
    assert len(opiniones) == 730
    assert opiniones[1].curso == 'Schwarz'
    assert opiniones[-1].curso == 'Kuhn'
