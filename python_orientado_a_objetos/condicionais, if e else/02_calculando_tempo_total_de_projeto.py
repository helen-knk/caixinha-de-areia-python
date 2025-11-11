def eh_negativo(valor):
    valor = int(valor)
    while valor < 0:
        print('Erro: Os dias não podem ser negativos.')
        valor = int(input('Digite novamente: '))
    return valor

def receber_dias_dos_projetos():
    atividade_a = eh_negativo(input('Informe os dias para a atividade A: '))
    atividade_b = eh_negativo(input('Informe os dias para a atividade B: '))
    atividade_c = eh_negativo(input('Informe os dias para a atividade C: '))
    return atividade_a, atividade_b, atividade_c

def calcular_tempo_total(atividade_a, atividade_b, atividade_c):
    return atividade_a + atividade_b + atividade_c

def main():
    atividade_a, atividade_b, atividade_c = receber_dias_dos_projetos()
    tempo = calcular_tempo_total(atividade_a, atividade_b, atividade_c)
    print(f'O tempo total do projeto foi de {tempo} dias.')

if __name__ == '__main__':
    main()
