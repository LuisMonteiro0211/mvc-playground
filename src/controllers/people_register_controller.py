from typing import Dict

class PeopleRegisterController:
    def register(self, new_person_information: Dict):
        try:
            #Validar os campos
            self.__validate_fields(new_person_information)
            #Enviar para models para cadastro de dados
            response = self.__format_response(new_person_information)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}


    def __validate_fields(self, new_person_information: Dict) -> None:
        name = new_person_information.get("name")
        age = new_person_information.get("age")
        height = new_person_information.get("height")

        # Validação do campo nome
        if name is None: 
            raise Exception('Campo nome é obrigatório!')
        if not isinstance(name, str):
            raise Exception('Campo nome deve ser uma string!')

        # Validação do campo idade
        if age is None: 
            raise Exception('Campo idade é obrigatório!')
        try: int(age)
        except: raise Exception('Campo idade deve ser um número inteiro!')

        # Validação do campo altura
        if height is None: 
            raise Exception('Campo altura é obrigatório!')
        try: int(height)
        except: raise Exception('Campo altura deve ser um número inteiro (cm)!')
    
    def __format_response(self, new_person_information: Dict) -> Dict:
        return {
            "message_success": "Pessoa cadastrada com sucesso!",
            "data": new_person_information
        }
