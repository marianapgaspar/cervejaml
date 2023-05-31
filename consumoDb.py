import sqlite3
import pandas
import datetime
import traceback
import sys


def criaTabela():
  conn = sqlite3.connect('baseDados.db')
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE consumo 
    (data DATETIME NOT NULL,
    dia_ano INTEGER NOT NULL,
    dia_semana INTEGER NOT NULL,
    semana_mes INTEGER NOT NULL,
    mes_ano INTEGER NOT NULL,
    final_semana INTEGER NOT NULL,
    temp_media FLOAT(5,2) NOT NULL,
    temp_min FLOAT(5,2) NOT NULL,
    temp_max FLOAT(5,2) NOT NULL,
    prec FLOAT(5,2) NOT NULL,
    consumo FLOAT NOT NULL);''')
  conn.close()


def insereDados(**kwargs):
  conn = sqlite3.connect('baseDados.db')

  data = kwargs['data']
  dia_ano = kwargs['dia_ano']
  dia_semana = kwargs['dia_semana']
  semana_mes = kwargs['semana_mes']
  mes_ano = kwargs['mes_ano']
  final_semana = kwargs['final_semana']
  temp_media = kwargs['temp_media']
  temp_min = kwargs['temp_min']
  temp_max = kwargs['temp_max']
  prec = kwargs['prec']
  consumo = kwargs['consumo']
  try:
    conn.execute(
      'INSERT INTO consumo (data, dia_ano, dia_semana,semana_mes, mes_ano, final_semana, temp_media, temp_min, temp_max,prec,consumo) VALUES ("'
      + str(data) + '",' + str(dia_ano) + ',' + str(dia_semana) + ',' +
      str(semana_mes) + ',' + str(mes_ano) + ',' + str(final_semana) + ',' +
      str(temp_media) + ',' + str(temp_min) + ',' + str(temp_max) + ',' +
      str(prec) + ',' + str(consumo) + ');')
    conn.commit()
  except sqlite3.Error as er:
    print('SQLite error: %s' % (' '.join(er.args)))
    print("Exception class is: ", er.__class__)
    print('SQLite traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
  conn.close()


def insereDadosDoCsv():
  tabela = pandas.read_csv("dados.csv")
  tabelaEditada = tabela.replace({',': '.'}, regex=True)
  for (i, row) in tabela.iterrows():
    dateArray = tabelaEditada['Data'][i].split("/")
    ano = int(dateArray[2])
    mes = int(dateArray[1])
    dia = int(dateArray[1])
    date = datetime.datetime(ano, mes, dia)
    insereDados(data=date,
                dia_ano=tabelaEditada['Dia do ano'][i],
                dia_semana=tabelaEditada['Dia da Semana'][i],
                semana_mes=tabelaEditada['Semana do mês'][i],
                mes_ano=tabelaEditada['Mes do ano'][i],
                final_semana=tabelaEditada['Final de Semana'][i],
                temp_media=tabelaEditada['Temperatura Media (C)'][i],
                temp_min=tabelaEditada['Temperatura Minima (C)'][i],
                temp_max=tabelaEditada['Temperatura Maxima (C)'][i],
                prec=tabelaEditada['Precipitacao (mm)'][i],
                consumo=tabelaEditada['Consumo de cerveja (litros)'][i])


def verTabelaConsumo():
  conn = sqlite3.connect('baseDados.db')
  try:
    cur = conn.cursor()
    cur.execute("SELECT * FROM consumo")
    rows = cur.fetchall()
    for row in rows:
      print(row)
  except sqlite3.Error as er:
    print('SQLite error: %s' % (' '.join(er.args)))
    print("Exception class is: ", er.__class__)
    print('SQLite traceback: ')
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))

  conn.close()
