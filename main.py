from flask import Flask, render_template, request
from machine import predicao

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/predicao', methods=['POST'])
def verificaPredicao():
  dia = request.form['dia']
  dia_semana = request.form['dia_semana']
  semana_mes = request.form['semana_mes']
  mes_ano = request.form['mes_ano']
  final_semana = request.form['final_semana']
  temp_media = request.form['temp_media']
  temp_min = request.form['temp_min']
  temp_max = request.form['temp_max']
  prec = request.form['prec']
  resultado = predicao(dia, dia_semana, semana_mes, mes_ano, final_semana,
                       temp_media, temp_min, temp_max, prec)
  return '{:.2f}'.format(float(resultado))


app.run(host='0.0.0.0', port=81)
