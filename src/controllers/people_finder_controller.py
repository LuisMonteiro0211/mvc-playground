from typing import Dict
from src.models.repository.person_repository import person_repository
from src.models.entities.person import Person

class PeopleFinderController:
    def find_by_name(self, person_finder_information: Dict) -> Dict:
        try:
            self.__validade_fields(person_finder_information)
            person = self.__find_person(person_finder_information)
            response = self.__format_response(person)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validade_fields(self, person_finder_information: Dict) -> None:
        finder_name = person_finder_information["finder_name"]
        
        if not isinstance(finder_name, str):
            raise Exception('Campo Nome Inválido!')

    def __find_person(self, person_finder_information: Dict) -> Person:
        name = person_finder_information["finder_name"]

        person = person_repository.find_person_by_name(name)
        if not person:
            raise Exception("Pessoa não encontrada")
        return person

    def __format_response(self, person: Person) -> Dict:
        return {
            "count": 1,
            "data": {
                "name": person.name,
                "age": person.age,
                "height": person.height
            }
        }
