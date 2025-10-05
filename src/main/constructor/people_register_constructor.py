from src.views.people_register_view import PeopleRegisterView
from src.controllers.people_register_controller import PeopleRegisterController

def people_register_constructor():
    #Instnaciamento das classes
    people_register_view = PeopleRegisterView()#Instancia a view
    people_register_controller = PeopleRegisterController()#Instancia a controller

    new_person_information = people_register_view.registry_person_view() #Chamada da view
    response = people_register_controller.register(new_person_information) #Chamada do controller

    if response.success:
        people_information = people_register_controller._people_information(response)
        return people_register_view.registry_person_success(people_information)


