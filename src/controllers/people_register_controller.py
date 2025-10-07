from src.models.types import PeopleInformation, PeopleFormatResponse, Response


class PeopleRegisterController:
    """Classe para registrar uma pessoa
    
    Methods:
        register: PeopleInformation -> Response

    Variables:
        new_person_information: PeopleInformation -> Dicionário com as informações da pessoa
    """

    def register(self, new_person_information: PeopleInformation) -> Response:
        """Função para registrar uma pessoa
        
        Args:
            new_person_information: PeopleInformation -> Dicionário com as informações da pessoa

        Returns:
            Response: Dicionário com o estado da aplicação e informações da pessoa
        """
        try:
            self.__validade_fields(new_person_information)
            #Futura chamada para o model
            response = self.__format_response(new_person_information)
            return Response(success = True, attributes = response, error = None)
        except Exception as exception:
            return Response(success = False, attributes=None, error = str(exception))

    def _people_information(self, response: Response) -> PeopleFormatResponse:
        """Retorna o dicionário PeopleFormatResponse de forma segura
        
        Args:
            response: Response -> Resposta da aplicação

        Returns:
            assert: PeopleFormatResponse -> Dicionário com o estado da aplicação e informações da pessoa de forma segura
        """
        assert response.attributes is not None and response.attributes['attributes'] is not None
        return response.attributes

    def __validade_fields(self, new_person_information: PeopleInformation):
        """Função para validar os campos do dicionário
        
        Utilizada para validar os campos do dicionário antes de enviar para a view  
        Args:
            new_person_information: PeopleInformation -> Dicionário com as informações da pessoa

        Raises:
            - Exception: Se o campo nome não foi uma string (str)
            - Exception: Se o campo idade não foi um inteiro (int)
            - Exception: Se o campo altura não foi um inteiro (int)
        """

        if not isinstance(new_person_information["name"], str):
            raise Exception('Campo nome incorreto!')
        
        try: int(new_person_information["age"])
        except: raise Exception('Campo idade incorreto!')

        try: int(new_person_information["height"])
        except: raise Exception('Campo altura incorreto!')

    def __format_response(self, new_person_information: PeopleInformation) -> PeopleFormatResponse:
        """Função para formatar a resposta
        
        Args:
            new_person_information: PeopleInformation -> Dicionário com as informações da pessoa

        Returns:
            PeopleFormatResponse: Dicionário com o estado da aplicação e informações da pessoa
        """
        message = PeopleFormatResponse(
            message = "Usuário cadastrado com sucesso!",
            attributes = new_person_information
        )
        return message
