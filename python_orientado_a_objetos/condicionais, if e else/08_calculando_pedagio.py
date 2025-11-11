distancia = float(input('Informe a distância percorrida (em km): '))

if distancia <= 100:
    print('O pedágio será R$ 10,00')
elif 100 < distancia <= 200:
    print('O pedágio será R$ 20,00')
else:
    print('O pedágio será R$ 30,00')
