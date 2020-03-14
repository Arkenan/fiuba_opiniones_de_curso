from flask import Flask, render_template, request
from app.excepcion_no_hay_datos import ExcepcionNoHayDatos
from app.opiniones_repo import OpinionesRepo
from app.asignaturas_repo import AsignaturasRepo
from app.periodo_repo import PeriodoRepo
from modelo.excepcion_cuatrimestre_no_valido import ExcepcionCuatrimestreNoValido
from modelo.periodo import Periodo
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html', periodos = PeriodoRepo().get_all())

@app.route('/periodo')
def periodo():
    anio, cuatrimestre = request.args.get('a'), request.args.get('c')
    try:
        periodo = Periodo(int(anio), int(cuatrimestre))
        opiniones = OpinionesRepo().opiniones_periodo(periodo)
        asignaturas = AsignaturasRepo().generar_desde_opiniones(opiniones)
        return render_template('periodo.html', asignaturas = asignaturas,
            periodo = periodo)
    except ExcepcionCuatrimestreNoValido:
        return 500, 'El cuatrimestre ingresado no es válido.'
    except ExcepcionNoHayDatos:
        return 500, 'No hay datos del período pedido.'

if __name__ == '__main__':
    app.run()
