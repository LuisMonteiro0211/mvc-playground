from src.views.people_finder_view import PeopleFinderView


def people_finder_constructor():
    people_finder_view = PeopleFinderView()
    #Futura chamada do controller

    people_finder_information = people_finder_view.find_person_view()
    #Enviar as informações para o controller
