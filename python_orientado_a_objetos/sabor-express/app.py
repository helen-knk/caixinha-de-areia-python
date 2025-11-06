import os
from nis import match

lista_restaurantes = \
    [{'nome': 'zorinho pizzaria', 'categoria': 'Pizza', 'ativo': True},
     {'nome': 'vó geralda congelados', 'categoria': 'Congelados', 'ativo': True}]

def exibir_nome_restaurante():
    print('''
    🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢
    ''')

def selecionar_opcoes():
    print('Opção 01: Cadastrar restaurante')
    print('Opção 02: Listar restaurantes')
    print('Opção 03: Ativar restaurante')
    print('Opção 04: Sair')

def finalizar_app():
    exibir_subtitulo('Finalizando o app...')

def voltar_ao_menu_principal():
    input('\nAperte ENTER para voltar ao menu principal')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('Opção inválida. Tente novamente.\n')
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    """Isso é uma docstring responsável por documentar o que a função realiza.
    Essa função é responsável por cadastrar novos restaurantes
    """
    exibir_subtitulo('Cadastro de novo restaurante')
    nome = input('Digite nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome}: ')
    dados_do_restaurante = {'nome': nome, 'categoria': categoria, 'ativo': False}
    lista_restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome} foi cadastrado com sucesso.')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Lista de restaurantes disponíveis:')
    print(f"{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(10)} | {'Status'}")
    for restaurante in lista_restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(10)} | {ativo}')
    voltar_ao_menu_principal()

def ativar_desativar_restaurante():
    exibir_subtitulo('Ativando ou destivando o restaurante...')
    nome_restaurante = input('Digite o nome do restaurante para encontrá-lo: ')
    restaurante_encontrado = False

    for restaurante in lista_restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f"{restaurante['nome']}, ativado com sucesso.")
    if not(restaurante_encontrado):
        print('Restaurante não encontrado.')

    voltar_ao_menu_principal()

def digitar_opcao():
    try:
        opcao = int(input('\n\nDigite uma opção: '))

        match opcao:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                ativar_desativar_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('clear')
    exibir_nome_restaurante()
    selecionar_opcoes()
    digitar_opcao()

if __name__ == '__main__':
    main()
