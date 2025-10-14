from typing import Dict
from os import system

class PeopleRegisterView:
    '''
    Classe para exibir a página de cadastro de pessoa
    '''
    def register_person_view(self) -> Dict:
        '''
        Função para exibir a página de cadastro de pessoa e retornar as informações da pessoa cadastrada
        
        Returns:
            Dict: As informações da pessoa cadastrada
        '''
        system("cls")

        print("*" * 35)
        print("MÓDULO 1 - CADASTRO DE PESSOA")
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
