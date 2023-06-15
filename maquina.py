import pandas
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pickle as pickle

nomeArquivo = '/var/www/cervejaml/modeloFinalizado.sav'


def criaModeloDoZero():
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

  modelo = linear_model.LinearRegression()
  modelo.fit(X_treino, y_treino)
  pickle.dump(modelo, open(nomeArquivo, 'wb'))


def exportaModeloReutilizado():
  regressao = pickle.load(open(nomeArquivo, 'rb'))
  return regressao
