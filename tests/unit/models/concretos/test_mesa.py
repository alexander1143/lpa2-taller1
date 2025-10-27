import pytest
from src.models.concretos.mesa import Mesa

class TestMesa:
    @pytest.fixture
    def mesa_basica(self):
        return Mesa(
            nombre="Mesa Básica",
            material="Madera",
            color="Café",
            precio_base=300.0,
            forma="rectangular",
            largo=150.0,
            ancho=90.0,
            altura=75.0,
            capacidad_personas=6
        )
    
    def test_inicializacion(self, mesa_basica):
        assert mesa_basica.nombre == "Mesa Básica"
        assert mesa_basica.material == "Madera"
        assert mesa_basica.forma == "rectangular"
        assert mesa_basica.capacidad_personas == 6
    
    def test_calcular_precio(self, mesa_basica):
        precio = mesa_basica.calcular_precio()
        # Precio base * factor tamaño + ajustes
        factor_tamaño = mesa_basica.calcular_factor_tamaño()
        precio_esperado = 300.0 * factor_tamaño
        # No hay ajuste por forma rectangular (es la forma base)
        # Ajuste por capacidad mayor a 4 personas
        precio_esperado += 100
        assert abs(precio - precio_esperado) < 0.01
    
    def test_forma_invalida(self):
        with pytest.raises(ValueError, match="Forma debe ser una de"):
            Mesa(
                nombre="Test",
                material="Madera",
                color="Café",
                precio_base=300.0,
                forma="triangular"
            )
    
    def test_validacion_capacidad(self):
        with pytest.raises(ValueError, match="La capacidad debe ser mayor a 0"):
            Mesa(
                nombre="Test",
                material="Madera",
                color="Café",
                precio_base=300.0,
                capacidad_personas=0
            )
    
    @pytest.mark.parametrize("forma,precio_extra", [
        ("rectangular", 0),
        ("redonda", 50),
        ("cuadrada", 50),
        ("ovalada", 50)
    ])
    def test_ajuste_forma(self, forma, precio_extra):
        mesa = Mesa(
            nombre="Test",
            material="Madera",
            color="Café",
            precio_base=100.0,
            forma=forma,
            largo=100.0,
            ancho=100.0,
            altura=75.0
        )
        precio = mesa.calcular_precio()
        factor_tamaño = mesa.calcular_factor_tamaño()
        precio_esperado = 100.0 * factor_tamaño + precio_extra
        assert abs(precio - precio_esperado) < 0.01
