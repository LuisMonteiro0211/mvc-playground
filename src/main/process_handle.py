from src.main.constructor.introduction_process import introduction_process
from time import sleep

def start() -> None:
    while True:
        command = introduction_process()

        if command == "1":
            print("Cadastrar usuário")
        elif command == "2":
            print("Pesquisar usuário")
        elif command == "5":
            print("Saindo...")
            sleep(1)
            exit()
        else:
            print("Comando inválido")
