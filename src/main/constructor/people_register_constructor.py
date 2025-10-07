from src.views.people_register_view import PeopleRegisterView
from src.controllers.people_register_controller import PeopleRegisterController

def people_register_constructor():    
    '''Função para construir o processo de registro de uma pessoa
    - Instancia a view e o controller
    - Chama a view para registrar uma pessoa
    - Chama o controller para registrar uma pessoa
    - Se a resposta for sucesso, chama a view para exibir a mensagem de sucesso
    - Se a resposta for falha, chama a view para exibir a mensagem de erro
    '''
    #Instnaciamento das classes
    people_register_view = PeopleRegisterView()#Instancia a view
    people_register_controller = PeopleRegisterController()#Instancia a controller

    new_person_information = people_register_view.registry_person_view() #Chamada da view
    response = people_register_controller.register(new_person_information) #Chamada do controller

    if response.success:
        people_information = people_register_controller._people_information(response)#Coleta a resposta do controller de forma segura
        people_register_view.registry_person_success(people_information)
    else:
        message_error = people_register_controller._get_error_message(response)#Coleta a mensagem de erro de forma segura
        people_register_view.registry_person_fail(message_error)
