import pandas
from math import log

total_respostas = 0
H = 0
porc_respostas = []

arq = pandas.read_csv('pesquisa_opiniao_times.csv')
classes = len(arq['time'])

for i in range(0, classes):
    total_respostas += arq['quantidade_respostas'][i]

for i in range(0, classes):
    x = arq['quantidade_respostas'][i]
    porc_respostas.append(x / total_respostas)

for i in range(0, classes):
    x = log(porc_respostas[i]) / log(2)
    H += porc_respostas[i] * x
    if i == 4:
        H *= -1

print(f"Resultado da entropia: {H}")
print(f"A entropia máxima é igual a: {log(classes, 2)}")
