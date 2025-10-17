from typing import Dict
from os import system

class PeopleFinderView:
    '''
    Classe para exibir a página de pesquisa de pessoa
    '''
    def find_person_view(self) -> Dict:
        '''
        Função para exibir a página de pesquisa de pessoa e retornar as informações da pessoa encontrada
        
        Returns:
            Dict: As informações da pessoa encontrada
        '''
        system("cls")

        print("*" * 35)
        print("MÓDULO 2 - PESQUISA DE PESSOA")
        print("*" * 35)

        finder_name = input("Determine o nome da pessoa para busca: ")

        person_finder_information = {
            "finder_name": finder_name
        }
        
        return person_finder_information

    def find_person_success(self, message: Dict) -> None:
        system("cls")
        data_person = message["message"]["data"]

        success_message = f'''
        Usuário encontrado com sucesso:

        Quantidade : {data_person["count"]}
        Informações:
            - Nome: {data_person["name"]}
        '''
        print(success_message)

    def find_person_fail(self, response: Dict) -> None:
        system("cls")
        error = response["error"]

        fail_message = f'''
        Falha ao encontrar usuário:

        Erro: {error}
        '''

        print(fail_message)

if __name__ == "__main__":
    PeopleFinderView().find_person_view()
