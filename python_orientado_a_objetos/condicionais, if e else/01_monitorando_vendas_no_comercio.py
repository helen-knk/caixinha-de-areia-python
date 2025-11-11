def receber_quantidade_vendas():
    maca = int(input('Digite a quantidade de maçãs vendidas: '))
    banana = int(input('Digite a quantidade de bananas vendidas: '))
    return maca, banana

def monitorar_venda_comercio(maca, banana):
    if maca > banana:
        print('As maçãs tiveram mais vendas.')
    elif maca < banana:
        print('As bananas tiveram mais vendas.')
    else:
        print('As vendas foram iguais.')

def main():
    maca, banana = receber_quantidade_vendas()
    monitorar_venda_comercio(maca, banana)

if __name__ == '__main__':
    main()
