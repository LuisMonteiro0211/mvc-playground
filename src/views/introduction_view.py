from pyfiglet import Figlet


def message_introduction():

    formatter = Figlet(font='small')
    print("*" * 80)
    print(f'{formatter.renderText("Sistema Cadastral")}')
    print("*" * 80)

def introduction_page() -> str:
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
