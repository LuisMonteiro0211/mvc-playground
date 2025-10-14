from pyfiglet import Figlet


def message_introduction() -> None:
    '''
    Função para exibir a mensagem de introdução do sistema
    '''
    formatter = Figlet(font='small')
    print("*" * 80)
    print(f'{formatter.renderText("Sistema Cadastral")}')
    print("*" * 80)

def introduction_page() -> str:
    '''
    Função para exibir a página de introdução do sistema e retornar o comando escolhido pelo usuário

    Returns:
        str: O comando escolhido pelo usuário
    '''
    message_introduction()
    message = '''

    * 1 -Cadastrar usuário
    * 2 -Pesquisar usuário
    * 5 -Sair
    '''
    print(message)
    command = input("Comando: ")

    return command

if __name__ == "__main__":
    introduction_page()
