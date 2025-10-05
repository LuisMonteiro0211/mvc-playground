from src.views.people_finder_view import PeopleFinderView

def people_finder_constructor():
    #Instnaciamento das classes
    people_finder_view = PeopleFinderView() #Instancia a view	
    #Futura instância da classe do controller

    person_finder_information = people_finder_view.finder_person_view()
    #Enviar para o controller
    
