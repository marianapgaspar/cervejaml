from flask import Flask, render_template, request
from predicao import predicao
import datetime
from consumoDb import insereDados

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/predicao', methods=['POST'])
def verificaPredicao():
  dateArray = request.form['date'].split("-")
  ano = int(dateArray[0])
  mes = int(dateArray[1])
  dia = int(dateArray[2])
  date = datetime.datetime(ano, mes, dia)
  dia = date.strftime("%j")
  dia_semana = int(date.strftime("%w")) + 1
  semana_mes = ((int(dia) - 1) / 7) + 1
  mes_ano = date.strftime("%m")
  if date.weekday() == 5 or date.weekday() == 6:
    final_semana = 1
  else:
    final_semana = 0
  temp_min = request.form['temp_min']
  temp_max = request.form['temp_max']
  temp_media = (float(temp_min) + float(temp_max)) / 2
  prec = request.form['prec']

  resultadoPredicao = predicao(dia=dia,
                               dia_semana=dia_semana,
                               semana_mes=semana_mes,
                               mes_ano=mes_ano,
                               final_semana=final_semana,
                               temp_media=temp_media,
                               temp_min=temp_min,
                               temp_max=temp_max,
                               prec=prec)

  insereDados(data=request.form['date'],
              dia_ano=dia,
              dia_semana=dia_semana,
              semana_mes=semana_mes,
              mes_ano=mes_ano,
              final_semana=final_semana,
              temp_media=temp_media,
              temp_min=temp_min,
              temp_max=temp_max,
              prec=prec,
              consumo=resultadoPredicao)

  return '{:.2f}'.format(float(resultadoPredicao))


if __name__ == "__main__":
    app.run()
