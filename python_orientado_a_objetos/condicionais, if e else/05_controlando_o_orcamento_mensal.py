limite = 3000
total_despesas = float(input('Digite o total de despesas do mês (R$): '))

if total_despesas > limite:
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print('Você está dentro do orçamento.')