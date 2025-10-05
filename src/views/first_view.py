import os

# Serve para mostrar/coletar informações ao usuário
# "Função burra" (Não tem lógica)

def introduction_page():
    os.system('cls')

    message = '''
        Sistema Cadastral

        * Cadastra Pessoa - 1
        * Buscas Pessoa Por Nome - 2
        * Sair - 5
    '''

    print(message)
    
    command = input('Comando: ')

    return command
