"""
Testes para o PeopleRegisterController
"""

import pytest
from src.controllers.people_register_controller import PeopleRegisterController
from src.models.types import PeopleInformation, Response


class TestPeopleRegisterController:
    """Classe de testes para PeopleRegisterController"""
    
    def setup_method(self):
        """Configuração antes de cada teste"""
        self.controller = PeopleRegisterController()
    
    def test_register_success(self):
        """Testa registro com dados válidos"""
        # Arrange
        valid_person = PeopleInformation(
            name="João Silva",
            age=25,
            height=175
        )
        
        # Act
        response = self.controller.register(valid_person)
        
        # Assert
        assert response.success is True
        assert response.error is None
        assert response.attributes is not None
        assert response.attributes["message"] == "Pessoa cadastrada com sucesso!"
        assert response.attributes["attributes"]["name"] == "João Silva"
        assert response.attributes["attributes"]["age"] == 25
        assert response.attributes["attributes"]["height"] == 175
    
    def test_register_invalid_name_type(self):
        """Testa registro com nome inválido (não string)"""
        # Arrange
        invalid_person = PeopleInformation(
            name=123,  # Nome como número
            age=25,
            height=175
        )
        
        # Act
        response = self.controller.register(invalid_person)
        
        # Assert
        assert response.success is False
        assert response.error == "Campo nome incorreto!"
        assert response.attributes is None
    
    def test_register_invalid_age_type(self):
        """Testa registro com idade inválida (não número)"""
        # Arrange
        invalid_person = PeopleInformation(
            name="João",
            age="vinte e cinco",  # Idade como string
            height=175
        )
        
        # Act
        response = self.controller.register(invalid_person)
        
        # Assert
        assert response.success is False
        assert response.error == "Campo idade incorreto!"
        assert response.attributes is None
    
    def test_register_invalid_height_type(self):
        """Testa registro com altura inválida (não número)"""
        # Arrange
        invalid_person = PeopleInformation(
            name="João",
            age=25,
            height="um metro e setenta"  # Altura como string
        )
        
        # Act
        response = self.controller.register(invalid_person)
        
        # Assert
        assert response.success is False
        assert response.error == "Campo altura incorreto!"
        assert response.attributes is None
    
    def test_people_information_success(self):
        """Testa _people_information com resposta de sucesso"""
        # Arrange
        success_response = Response(
            success=True,
            attributes={
                "message": "Pessoa cadastrada com sucesso!",
                "attributes": {
                    "name": "João",
                    "age": 25,
                    "height": 175
                }
            },
            error=None
        )
        
        # Act
        result = self.controller._people_information(success_response)
        
        # Assert
        assert result["message"] == "Pessoa cadastrada com sucesso!"
        assert result["attributes"]["name"] == "João"
        assert result["attributes"]["age"] == 25
        assert result["attributes"]["height"] == 175
    
    def test_people_information_with_none_attributes(self):
        """Testa _people_information com attributes None (deve falhar)"""
        # Arrange
        error_response = Response(
            success=False,
            attributes=None,
            error="Erro de validação"
        )
        
        # Act & Assert
        with pytest.raises(AssertionError):
            self.controller._people_information(error_response)
