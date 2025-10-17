from src.views.people_finder_view import PeopleFinderView
from src.controllers.people_finder_controller import PeopleFinderController


def people_finder_constructor():
    people_finder_view = PeopleFinderView()
    people_finder_controller = PeopleFinderController()

    people_finder_information = people_finder_view.find_person_view()
    response = people_finder_controller.find_by_name(people_finder_information)

    if response["success"]:
        people_finder_view.find_person_success(response)
    else:
        people_finder_view.find_person_fail(response)
