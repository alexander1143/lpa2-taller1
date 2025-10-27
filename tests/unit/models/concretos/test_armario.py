import pytest
from src.models.concretos.armario import Armario

class TestArmario:
    @pytest.fixture
    def armario_basico(self):
        return Armario(
            nombre="Armario Básico",
            material="Madera",
            color="Café",
            precio_base=300.0,
            altura=180.0,
            ancho=100.0,
            profundidad=60.0,
            num_compartimentos=4,
            num_puertas=2,
            tipo_puertas="batientes"
        )
    
    def test_inicializacion(self, armario_basico):
        assert armario_basico.nombre == "Armario Básico"
        assert armario_basico.material == "Madera"
        assert armario_basico.num_puertas == 2
        assert armario_basico.tipo_puertas == "batientes"
    
    def test_calcular_precio(self, armario_basico):
        precio = armario_basico.calcular_precio()
        # Precio base * factor volumen * factor puertas
        factor_volumen = armario_basico.calcular_factor_volumen()
        precio_esperado = 300.0 * factor_volumen
        # Factor adicional por puertas corredizas (no aplicable en este caso)
        assert abs(precio - precio_esperado) < 0.01
    
    def test_validacion_puertas(self):
        with pytest.raises(ValueError, match="El número de puertas debe ser mayor a 0"):
            Armario(
                nombre="Test",
                material="Madera",
                color="Café",
                precio_base=300.0,
                altura=180.0,
                ancho=100.0,
                profundidad=60.0,
                num_puertas=0
            )
    
    def test_tipo_puertas_invalido(self):
        with pytest.raises(ValueError, match="Tipo de puertas debe ser uno de"):
            Armario(
                nombre="Test",
                material="Madera",
                color="Café",
                precio_base=300.0,
                altura=180.0,
                ancho=100.0,
                profundidad=60.0,
                tipo_puertas="giratorias"
            )
    
    def test_puertas_corredizas_precio(self):
        armario = Armario(
            nombre="Armario Corredizo",
            material="Madera",
            color="Café",
            precio_base=300.0,
            altura=180.0,
            ancho=100.0,
            profundidad=60.0,
            tipo_puertas="corredizas"
        )
        precio_base = armario.calcular_precio()
        # Las puertas corredizas aumentan el precio en un 20%
        assert precio_base > 300.0
