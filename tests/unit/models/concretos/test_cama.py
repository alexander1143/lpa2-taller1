import pytest
from src.models.concretos.cama import Cama

class TestCama:
    @pytest.fixture
    def cama_basica(self):
        return Cama(
            nombre="Cama Básica",
            material="Madera",
            color="Café",
            precio_base=400.0,
            tamaño="matrimonial",
            incluye_colchon=True,
            tiene_cabecera=True
        )
    
    def test_inicializacion(self, cama_basica):
        assert cama_basica.nombre == "Cama Básica"
        assert cama_basica.material == "Madera"
        assert cama_basica.tamaño == "matrimonial"
        assert cama_basica.incluye_colchon is True
        assert cama_basica.tiene_cabecera is True
    
    def test_calcular_precio(self, cama_basica):
        precio = cama_basica.calcular_precio()
        # Precio base + extras por tamaño y accesorios
        precio_esperado = 400.0 * 1.3  # 30% extra por matrimonial
        precio_esperado *= 1.15  # 15% extra por colchón
        precio_esperado *= 1.1  # 10% extra por cabecera
        assert abs(precio - precio_esperado) < 0.01
    
    def test_tamaño_invalido(self):
        with pytest.raises(ValueError, match="Tamaño debe ser uno de"):
            Cama(
                nombre="Test",
                material="Madera",
                color="Café",
                precio_base=400.0,
                tamaño="gigante"
            )
    
    @pytest.mark.parametrize("tamaño,factor", [
        ("individual", 1.0),
        ("matrimonial", 1.3),
        ("queen", 1.5),
        ("king", 1.7)
    ])
    def test_factor_tamaño(self, tamaño, factor):
        cama = Cama(
            nombre="Test",
            material="Madera",
            color="Café",
            precio_base=100.0,
            tamaño=tamaño,
            incluye_colchon=False,
            tiene_cabecera=False
        )
        precio = cama.calcular_precio()
        assert abs(precio - (100.0 * factor)) < 0.01
    
    def test_sin_accesorios(self):
        cama = Cama(
            nombre="Cama Básica",
            material="Madera",
            color="Café",
            precio_base=400.0,
            incluye_colchon=False,
            tiene_cabecera=False
        )
        precio = cama.calcular_precio()
        # Solo precio base * factor tamaño individual
        assert precio == 400.0
