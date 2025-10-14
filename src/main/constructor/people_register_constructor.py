from src.views.people_register_view import PeopleRegisterView

def people_register_constructor():
    people_register_view = PeopleRegisterView()
    #Futura chamada do controller

    people_register_information = people_register_view.register_person_view()
    #Enviar as informações para o controller
