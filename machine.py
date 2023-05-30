import pandas
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import numpy as np

tabela = pandas.read_csv("dados.csv")

X_treino, X_teste, y_treino, y_teste = train_test_split(
  tabela[[
    'Dia', 'Dia da Semana', 'Semana do mês', 'Mes do ano', 'Final de Semana',
    'Temperatura Media (C)', 'Temperatura Minima (C)',
    'Temperatura Maxima (C)', 'Precipitacao (mm)'
  ]].values,
  tabela[['Consumo de cerveja (litros)']].values,
  test_size=0.15,
  random_state=40)

regressao = linear_model.LinearRegression()
regressao.fit(X_treino, y_treino)


def predicao(**kwargs):
  dia = kwargs['dia']
  dia_semana = kwargs['dia_semana']
  semana_mes = kwargs['semana_mes']
  mes_ano = kwargs['mes_ano']
  final_semana = kwargs['final_semana']
  temp_media = kwargs['temp_media']
  temp_min = kwargs['temp_min']
  temp_max = kwargs['temp_max']
  prec = kwargs['prec']
  a = [
    dia, dia_semana, semana_mes, mes_ano, final_semana, temp_media, temp_min,
    temp_max, prec
  ]  #  non-numeric format
  b = np.array(a, dtype=float)  #  convert using numpy
  c = [[float(i) for i in a]]
  predicao = regressao.predict(c)
  return str(predicao[0][0])
