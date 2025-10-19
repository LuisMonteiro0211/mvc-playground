from typing import List, Optional
from src.models.entities.person import Person

##Local onde interagimos com o banco de dados e os dados da aplicação 

class PersonRepository:
    def __init__(self) -> None:
        self.__people: List = []

    def registry_person(self, person: Person) -> None:
        self.__people.append(person)

    def find_person_by_name(self, name: str) -> Optional[Person]:
        for person in self.__people:
            if person.name == name:
                return person
        return None

person_repository = PersonRepository()
