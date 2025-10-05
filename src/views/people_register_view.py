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
        os.system('cls')
        
            
    def registry_person_fail(self, message: Response) -> None:
        """Função para exibir a mensagem de erro
        
        Args:
            message: Response -> Mensagem de erro
        """
        os.system('cls')
        message_error = message.error #Coleta a mensagem de erro

        print(f'''
        Falha ao cadastrar usuário
        
        Erro: {message_error}
        ''')


if __name__ == '__main__':
    people_register_view = PeopleRegisterView()
    new_person = people_register_view.registry_person_view()
    print(new_person)
