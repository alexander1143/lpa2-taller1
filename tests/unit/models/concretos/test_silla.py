import pytest
from src.models.concretos.silla import Silla

class TestSilla:
    @pytest.fixture
    def silla_basica(self):
        return Silla("Silla Básica", "Madera", "Marrón", 50.0, True)
    
    def test_instanciacion_correcta(self, silla_basica):
        # Verificar herencia de atributos
        assert silla_basica.nombre == "Silla Básica"
        assert silla_basica.material == "Madera"
        assert silla_basica.color == "Marrón"
        assert silla_basica.precio_base == 50.0
        
        # Verificar atributos específicos
        assert silla_basica.tiene_respaldo is True
    
    def test_calcular_precio(self, silla_basica):
        # El precio incluye factores de modificación por tener respaldo
        precio = silla_basica.calcular_precio()
        precio_esperado = 50.0 * 1.1  # 10% extra por tener respaldo
        assert abs(precio - precio_esperado) < 0.01  # Comparación con margen de error
    
    def test_obtener_descripcion(self, silla_basica):
        descripcion = silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
        assert "Madera" in descripcion