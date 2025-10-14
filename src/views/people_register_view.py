from typing import Dict
from os import system

class PeopleRegisterView:
    def register_person_view(self) -> Dict:
        system("cls")

        print("*" * 35)
        print("MÓDULO 2 - CADASTRO DE PESSOA")
        print("*" * 35)

        name = input("Digite o nome da pessoa: ")
        age = input("Digite a idade da pessoa: ")
        height = input("Digite a altura da pessoa: ")

        new_person_information = {
            "name": name,
            "age": age,
            "height": height
        }
        
        return new_person_information

if __name__ == "__main__":
    PeopleRegisterView().register_person_view()
