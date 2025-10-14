from src.main.constructor.introduction_process import introduction_process
from src.main.constructor.people_register_constructor import people_register_constructor
from src.main.constructor.people_finder_constructor import people_finder_constructor
from time import sleep

def start() -> None:
    while True:
        command = introduction_process()

        if command == "1":
            people_register_constructor()
        elif command == "2":
            people_finder_constructor()
        elif command == "5":
            print("Saindo...")
            sleep(1)
            exit()
        else:
            print("\n Comando inválido!! \n\n")
