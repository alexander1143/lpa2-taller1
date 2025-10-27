import pytest
from src.models.concretos.cajonera import Cajonera

class TestCajonera:
    @pytest.fixture
    def cajonera_basica(self):
        return Cajonera(
            nombre="Cajonera Básica",
            material="Madera",
            color="Blanco",
            precio_base=200.0,
            altura=100.0,
            ancho=50.0,
            profundidad=40.0,
            num_compartimentos=4,
            num_cajones=4,
            tiene_ruedas=True
        )
    
    def test_inicializacion(self, cajonera_basica):
        assert cajonera_basica.nombre == "Cajonera Básica"
        assert cajonera_basica.material == "Madera"
        assert cajonera_basica.num_cajones == 4
        assert cajonera_basica.tiene_ruedas is True
    
    def test_calcular_precio(self, cajonera_basica):
        precio = cajonera_basica.calcular_precio()
        # Precio base * factor volumen * (1 + 0.1 por ruedas)
        factor_volumen = cajonera_basica.calcular_factor_volumen()
        precio_esperado = 200.0 * factor_volumen * 1.1  # 10% extra por ruedas
        assert abs(precio - precio_esperado) < 0.01
    
    def test_validacion_cajones(self):
        with pytest.raises(ValueError, match="El número de cajones debe ser mayor a 0"):
            Cajonera(
                nombre="Test",
                material="Madera",
                color="Blanco",
                precio_base=200.0,
                altura=100.0,
                ancho=50.0,
                profundidad=40.0,
                num_cajones=0
            )
    
    def test_sin_ruedas_precio(self):
        cajonera = Cajonera(
            nombre="Cajonera Sin Ruedas",
            material="Madera",
            color="Blanco",
            precio_base=200.0,
            altura=100.0,
            ancho=50.0,
            profundidad=40.0,
            tiene_ruedas=False
        )
        precio_sin_ruedas = cajonera.calcular_precio()
        
        cajonera.tiene_ruedas = True
        precio_con_ruedas = cajonera.calcular_precio()
        
        assert precio_con_ruedas > precio_sin_ruedas
