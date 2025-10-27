import pytest
from src.models.concretos.escritorio import Escritorio

class TestEscritorio:
    @pytest.fixture
    def escritorio_basico(self):
        return Escritorio(
            nombre="Escritorio Básico",
            material="Madera",
            color="Café",
            precio_base=250.0,
            largo=120.0,
            ancho=60.0,
            altura=75.0,
            tiene_cajonera=True,
            porta_teclado=True,
            tipo="ejecutivo"
        )
    
    def test_inicializacion(self, escritorio_basico):
        assert escritorio_basico.nombre == "Escritorio Básico"
        assert escritorio_basico.material == "Madera"
        assert escritorio_basico.tiene_cajonera is True
        assert escritorio_basico.porta_teclado is True
        assert escritorio_basico.tipo == "ejecutivo"
    
    def test_calcular_precio(self, escritorio_basico):
        precio = escritorio_basico.calcular_precio()
        # Precio base * factor tamaño * factores adicionales
        factor_tamaño = escritorio_basico.calcular_factor_tamaño()
        precio_esperado = 250.0 * factor_tamaño
        precio_esperado *= 1.2  # 20% extra por cajonera
        precio_esperado *= 1.1  # 10% extra por porta teclado
        assert abs(precio - precio_esperado) < 0.01
    
    def test_tipo_invalido(self):
        with pytest.raises(ValueError, match="Tipo de escritorio debe ser uno de"):
            Escritorio(
                nombre="Test",
                material="Madera",
                color="Café",
                precio_base=250.0,
                largo=120.0,
                ancho=60.0,
                altura=75.0,
                tipo="gaming"
            )
    
    @pytest.mark.parametrize("tipo,tiene_cajonera,porta_teclado,factor_extra", [
        ("estudiante", False, False, 1.0),
        ("ejecutivo", True, True, 1.2 * 1.1),
        ("esquinero", True, False, 1.2),
        ("estudiante", False, True, 1.1)
    ])
    def test_configuraciones_precio(self, tipo, tiene_cajonera, porta_teclado, factor_extra):
        escritorio = Escritorio(
            nombre="Test",
            material="Madera",
            color="Café",
            precio_base=100.0,
            largo=120.0,
            ancho=60.0,
            altura=75.0,
            tipo=tipo,
            tiene_cajonera=tiene_cajonera,
            porta_teclado=porta_teclado
        )
        precio = escritorio.calcular_precio()
        factor_tamaño = escritorio.calcular_factor_tamaño()
        precio_esperado = 100.0 * factor_tamaño * factor_extra
        assert abs(precio - precio_esperado) < 0.01
