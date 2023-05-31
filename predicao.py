import numpy as np
from maquina import exportaModeloReutilizado

regressao = exportaModeloReutilizado()


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
