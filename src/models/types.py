from typing  import TypedDict, Optional
from dataclasses import dataclass

class PeopleInformation(TypedDict):
    """Classe para representar as informações de uma pessoa
    
    Variables:
        name: str
        age: int
        height: int
    """
    name: str
    age: int
    height: int

class PeopleFormatResponse(TypedDict):
    """Classe para representar a resposta de sucesso de uma pessoa
    
    Variables:
        message: str
        attributes: PeopleInformation
    """
    message: str
    attributes: PeopleInformation

@dataclass
class Response:
    success: bool
    attributes: Optional[PeopleFormatResponse] = None
    error: Optional[str] = None
