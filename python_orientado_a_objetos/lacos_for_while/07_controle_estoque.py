livro_estoque_inicial = 5

while livro_estoque_inicial > 0:
    venda = int(input('Quantos examplares foram vendidos? '))
    if livro_estoque_inicial >= venda:
        livro_estoque_inicial = livro_estoque_inicial - venda
        print(f'Venda realizada! Estoque restante: {livro_estoque_inicial}')
    else:
        print(f'Venda maior que o estoque disponível {livro_estoque_inicial}')
print('Estoque esgotado')