import pytest
from src.models.concretos.sillon import Sillon

class TestSillon:
    @pytest.fixture
    def sillon_basico(self):
        return Sillon(
            nombre="Sillón Básico",
            material="Tela",
            color="Gris",
            precio_base=400.0,
            es_reclinable=True,
            tiene_masajeador=False,
            material_tapizado="tela"
        )
    
    def test_inicializacion(self, sillon_basico):
        assert sillon_basico.nombre == "Sillón Básico"
        assert sillon_basico.material == "Tela"
        assert sillon_basico.es_reclinable is True
        assert sillon_basico.tiene_masajeador is False
        assert sillon_basico.material_tapizado == "tela"
    
    def test_calcular_precio(self, sillon_basico):
        precio = sillon_basico.calcular_precio()
        # Precio base * factor comodidad * factores adicionales
        factor_comodidad = sillon_basico.calcular_factor_comodidad()
        precio_esperado = 400.0 * factor_comodidad
        precio_esperado *= 1.2  # 20% extra por ser reclinable
        assert abs(precio - precio_esperado) < 0.01
    
    def test_sillon_full_extras(self):
        sillon = Sillon(
            nombre="Sillón Premium",
            material="Cuero",
            color="Negro",
            precio_base=400.0,
            es_reclinable=True,
            tiene_masajeador=True,
            material_tapizado="cuero"
        )
        precio = sillon.calcular_precio()
        # Debe ser significativamente más caro que el básico
        # Con todos los extras debe ser al menos 50% más caro que el precio base
        assert precio > 400.0 * 1.5
    
    def test_sin_extras(self):
        sillon = Sillon(
            nombre="Sillón Básico",
            material="Tela",
            color="Gris",
            precio_base=400.0,
            es_reclinable=False,
            tiene_masajeador=False
        )
        precio = sillon.calcular_precio()
        # Solo precio base * factor comodidad base
        factor_comodidad = sillon.calcular_factor_comodidad()
        precio_esperado = 400.0 * factor_comodidad
        assert abs(precio - precio_esperado) < 0.01
    
    @pytest.mark.parametrize("material,reclinable,masajeador,factor_extra", [
        ("tela", False, False, 1.0),
        ("tela", True, False, 1.2),
        ("cuero", False, True, 1.3),
        ("cuero", True, True, 1.2 * 1.3)
    ])
    def test_combinaciones_caracteristicas(self, material, reclinable, masajeador, factor_extra):
        sillon = Sillon(
            nombre="Test",
            material=material,
            color="Negro",
            precio_base=100.0,
            es_reclinable=reclinable,
            tiene_masajeador=masajeador,
            material_tapizado=material
        )
        precio = sillon.calcular_precio()
        factor_comodidad = sillon.calcular_factor_comodidad()
        precio_esperado = 100.0 * factor_comodidad * factor_extra
        assert abs(precio - precio_esperado) < 0.01
