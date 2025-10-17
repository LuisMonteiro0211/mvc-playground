from typing import Dict

class PeopleFinderController:
    def find_by_name(self, person_finder_information: Dict) -> Dict:
        try:
            self.__validade_fields(person_finder_information)
            #Buscar em banco de dados
            response = self.__format_response(None)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __validade_fields(self, person_finder_information: Dict) -> None:
        finder_name = person_finder_information["finder_name"]
        
        if not isinstance(finder_name, str):
            raise Exception('Campo Nome Inválido!')
        
    def __format_response(self, person) -> Dict:
        return {
            "count": 1,
            "data": {
                "name": "Teste de nome"
            }
        }
