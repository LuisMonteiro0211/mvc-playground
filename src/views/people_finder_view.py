import os
from typing import Dict

class PeopleFinderView:
    '''Classe para buscar uma pessoa
    
        Methods:
            finder_person_view: Dict -> Dict
    '''

    def finder_person_view(self) -> Dict:

        os.system('cls')

        print('Buscar Pessoa \n\n')
        name = input('Informa o nome da pessoa: ')

        person_finder_information = {
            'name': name
        }

        return person_finder_information

if __name__ == '__main__':
    people_finder_view = PeopleFinderView()
    person_finder_information = people_finder_view.finder_person_view()
    print(person_finder_information)      
