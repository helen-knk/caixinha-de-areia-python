projetos = ['website', 'jogo', 'análise de dados', None, 'aplicativo móvel']

for projeto in projetos:
    print(projeto) if projeto is not None else print('Projeto ausente')
