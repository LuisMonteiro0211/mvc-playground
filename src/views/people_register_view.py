from typing import Dict
from os import system

class PeopleRegisterView:
    '''
    Agrupamento de "páginas" relacionadas ao cadastro de pessoas

    OBS: Cada "página" deve ser uma função separada, e o sistema deve ser modularizado, ou seja, cada módulo deve ser um arquivo separado.

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
            "age": int(age),
            "height": float(height)
        }
        
        return new_person_information

    def register_person_success(self, response: Dict) -> None:
        system("cls")
        message_success = response["message"]["message_success"]
        data_person = response["message"]["data"]
        name = data_person["name"]
        age = data_person["age"]
        height = data_person["height"]

        message = f'''
        {message_success}

        Informações da pessoa:
        Nome: {name}
        Idade: {age}
        Altura: {height}
        '''

        print(message)

    def register_person_fail(self, response: Dict) -> None:
        system("cls")
        message_error = response["error"]

        fail_message = f'''
        Falha ao cadastrar usuário:

        Erro: {message_error}
        '''
        print(fail_message)

if __name__ == "__main__":
    PeopleRegisterView().register_person_view()
