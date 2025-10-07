import os
from src.models.types import PeopleInformation, PeopleFormatResponse, Response

class PeopleRegisterView:
    '''Classe para registrar uma pessoa
    
        Methods:
            registry_person_view: Dictionary -> Dictionary
    '''

    def registry_person_view(self) -> PeopleInformation:
        os.system('cls')

        print('Cadastra Nova Pessoa \n\n')
        name = input('Informe o nome: ')
        age = int(input('Informe a idade: '))
        height = int(input('Informe a altura: '))

        new_person = PeopleInformation(
            name = name,
            age = age,
            height = height
        )

        return new_person

    def registry_person_success(self, message: PeopleFormatResponse) -> None:
        """Função para exibir a mensagem de sucesso
        
        Args:
            message: Response -> Mensagem de sucesso
        """
        message_success = message['message']
        message_name = message['attributes']['name']
        message_age = message['attributes']['age']
        message_height = message['attributes']['height']
        
        os.system('cls')
        success_message = f'''
        {message_success}

        Informações do usuário:
        Nome: {message_name}
        Idade: {message_age}
        Altura: {message_height}
        
        '''
        print(success_message)
            
    def registry_person_fail(self, error: Response) -> None:
        """Função para exibir a mensagem de erro
        
        Args:
            message: Response -> Mensagem de erro
        """
        os.system('cls')
        error_message = error.error #Coleta a mensagem de erro

        message_fail = f'''
        Falha ao cadastrar usuário
        
        Erro: {error_message:=^30}!
        '''

        print(message_fail)

if __name__ == '__main__':
    people_register_view = PeopleRegisterView()
    new_person = people_register_view.registry_person_view()
    print(new_person)
