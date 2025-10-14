from typing import Dict
from os import system

class PeopleFinderView:
    def find_person_view(self) -> Dict:
        system("cls")

        print("*" * 35)
        print("MÓDULO 1 - PESQUISA DE PESSOA")
        print("*" * 35)

        finder_name = input("Determine o nome da pessoa para busca: ")

        person_finder_information = {
            "finder_name": finder_name
        }
        
        return person_finder_information

if __name__ == "__main__":
    PeopleFinderView().find_person_view()
