renda = float(input('Digite o valor da sua renda mensal: '))
parcela = float(input('Digite o valor da parcela desejada: '))

valor_parcela_permitida = renda * 0.3

if renda >= 2000 and valor_parcela_permitida >= parcela:
    print('Empréstimo aprovado!')
elif renda <= 2000:
    print('Empréstimo negado: renda insuficiente.')
else:
    print('Empréstimo negado: parcela acima de 30% da renda.')
