while True:
    user_name = input('Digite seu nome de usuário: ')
    user_password = input('Digite a sua senha: ')

    if len(user_name) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.')
        continue

    if len(user_password) < 8:
        print('A senha deve ter pelo menos 8 caracteres.')
        continue

    print('Cadastro realizado com sucesso!')
    break
