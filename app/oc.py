from flask import Flask, render_template
from app.periodo_repo import PeriodoRepo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', periodos = PeriodoRepo().get_all())

if __name__ == '__main__':
    app.run()
