## Representação dos dados que serão armazenados durante o processo de cadastro de pessoa

class Person:
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self) -> str:
        """Retorna uma representação legível do objeto para o usuário"""
        return f"Person(name='{self.name}', age={self.age}, height={self.height}m)"
    
    def __repr__(self) -> str:
        """Retorna uma representação técnica do objeto (útil para debug)"""
        return f"Person(name='{self.name}', age={self.age}, height={self.height}m)"
