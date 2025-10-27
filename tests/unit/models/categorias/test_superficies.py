import pytest
from src.models.categorias.superficies import Superficie

class TestSuperficies:
    @pytest.fixture
    def superficie_basica(self):
        class SuperficieConcreto(Superficie):
            def calcular_precio(self) -> float:
                return self.precio_base * self.calcular_factor_tamaño()
            
            def obtener_descripcion(self) -> str:
                return "Superficie para pruebas"
        
        return SuperficieConcreto(
            nombre="Superficie Test",
            material="Madera",
            color="Café",
            precio_base=100.0,
            largo=120.0,
            ancho=80.0,
            altura=75.0
        )
    
    def test_inicializacion(self, superficie_basica):
        assert superficie_basica.largo == 120.0
        assert superficie_basica.ancho == 80.0
        assert superficie_basica.altura == 75.0
    
    def test_calcular_area(self, superficie_basica):
        area = superficie_basica.calcular_area()
        assert area == 120.0 * 80.0  # largo * ancho
    
    def test_calcular_factor_tamaño(self, superficie_basica):
        factor = superficie_basica.calcular_factor_tamaño()
        area = superficie_basica.calcular_area()
        # Factor base 1.0 + 0.1 por cada 5000 cm²
        factor_esperado = 1.0 + (area / 5000) * 0.1
        assert abs(factor - factor_esperado) < 0.01
    
    def test_validacion_dimensiones(self):
        class SuperficieConcreto(Superficie):
            def calcular_precio(self) -> float:
                return self.precio_base
            
            def obtener_descripcion(self) -> str:
                return "Superficie para pruebas"
        
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            SuperficieConcreto(
                nombre="Test",
                material="Madera",
                color="Café",
                precio_base=100.0,
                largo=-1,
                ancho=80.0,
                altura=75.0
            )
    
    def test_calcular_factor_tamaño_minimo(self):
        class SuperficieConcreto(Superficie):
            def calcular_precio(self) -> float:
                return self.precio_base
            
            def obtener_descripcion(self) -> str:
                return "Superficie para pruebas"
        
        superficie = SuperficieConcreto(
            nombre="Test",
            material="Madera",
            color="Café",
            precio_base=100.0,
            largo=10.0,
            ancho=10.0,
            altura=75.0
        )
        # Para áreas muy pequeñas, el factor debe ser al menos 1.0
        assert superficie.calcular_factor_tamaño() == 1.0
