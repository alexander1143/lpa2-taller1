import pytest
from src.models.concretos.sofa import Sofa

class TestSofa:
    @pytest.fixture
    def sofa_basico(self):
        return Sofa(
            nombre="Sofá Básico",
            material="Tela",
            color="Gris",
            precio_base=500.0,
            capacidad_personas=3,
            tiene_respaldo=True,
            material_tapizado="tela",
            tiene_brazos=True,
            es_modular=False,
            incluye_cojines=True
        )
    
    def test_inicializacion(self, sofa_basico):
        assert sofa_basico.nombre == "Sofá Básico"
        assert sofa_basico.material == "Tela"
        assert sofa_basico.tiene_brazos is True
        assert sofa_basico.es_modular is False
        assert sofa_basico.incluye_cojines is True
    
    def test_calcular_precio(self, sofa_basico):
        precio = sofa_basico.calcular_precio()
        # Precio base * factor comodidad * factores adicionales
        factor_comodidad = sofa_basico.calcular_factor_comodidad()
        precio_esperado = 500.0 * factor_comodidad
        # 10% extra por brazos, 10% por cojines
        precio_esperado *= 1.1 * 1.1
        assert abs(precio - precio_esperado) < 0.01
    
    def test_sofa_modular(self):
        sofa = Sofa(
            nombre="Sofá Modular",
            material="Tela",
            color="Gris",
            precio_base=500.0,
            es_modular=True
        )
        precio = sofa.calcular_precio()
        # El precio debe ser mayor por ser modular
        precio_base = 500.0 * sofa.calcular_factor_comodidad()
        assert precio > precio_base * 1.2
    
    def test_sofa_cuero_premium(self):
        sofa = Sofa(
            nombre="Sofá Premium",
            material="Cuero",
            color="Negro",
            precio_base=500.0,
            material_tapizado="cuero",
            tiene_brazos=True,
            incluye_cojines=True
        )
        precio = sofa.calcular_precio()
        # Debe ser más caro que el sofá básico de tela
        # El sofá de cuero debe ser al menos 30% más caro que el precio base
        assert precio > 500.0 * 1.3
    
    @pytest.mark.parametrize("config", [
        {"es_modular": True, "incluye_cojines": True},
        {"es_modular": False, "incluye_cojines": True},
        {"es_modular": True, "incluye_cojines": False},
        {"tiene_brazos": False, "incluye_cojines": True}
    ])
    def test_configuraciones_precio(self, config):
        sofa = Sofa(
            nombre="Test",
            material="Tela",
            color="Gris",
            precio_base=100.0,
            **config
        )
        precio = sofa.calcular_precio()
        # Verificar que el precio es positivo y refleja la configuración
        assert precio > 100.0
