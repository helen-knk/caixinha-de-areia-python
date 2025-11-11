nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))
nota_tres = float(input('Digite a terceira nota: '))

media = (nota_um + nota_dois + nota_tres) / 3

if media >= 7:
    print('Aprovado')
elif 5 <= media < 7:
    print('Recuperação')
else:
    print('Reprovado')
