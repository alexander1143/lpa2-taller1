import pytest
from src.models.categorias.asientos import Asiento

class TestAsientos:
    @pytest.fixture
    def asiento_basico(self):
        class AsientoConcreto(Asiento):
            def calcular_precio(self) -> float:
                return self.precio_base * self.calcular_factor_comodidad()
            
            def obtener_descripcion(self) -> str:
                return "Asiento para pruebas"
        
        return AsientoConcreto(
            nombre="Asiento Test",
            material="Tela",
            color="Azul",
            precio_base=100.0,
            capacidad_personas=2,
            tiene_respaldo=True,
            material_tapizado="tela"
        )
    
    def test_inicializacion(self, asiento_basico):
        assert asiento_basico.capacidad_personas == 2
        assert asiento_basico.tiene_respaldo is True
        assert asiento_basico.material_tapizado == "tela"
    
    def test_calcular_factor_comodidad(self, asiento_basico):
        factor = asiento_basico.calcular_factor_comodidad()
        # Factor base 1.0 + 0.1 por respaldo + 0.1 por material tela
        assert factor == 1.2
    
    def test_factor_comodidad_cuero(self):
        class AsientoConcreto(Asiento):
            def calcular_precio(self) -> float:
                return self.precio_base
            
            def obtener_descripcion(self) -> str:
                return "Asiento para pruebas"
        
        asiento = AsientoConcreto(
            nombre="Test",
            material="Cuero",
            color="Negro",
            precio_base=100.0,
            material_tapizado="cuero"
        )
        factor = asiento.calcular_factor_comodidad()
        # Factor base 1.0 + 0.2 por material cuero
        assert factor == 1.2
    
    def test_validacion_capacidad_personas(self):
        class AsientoConcreto(Asiento):
            def calcular_precio(self) -> float:
                return self.precio_base
            
            def obtener_descripcion(self) -> str:
                return "Asiento para pruebas"
        
        with pytest.raises(ValueError, match="La capacidad debe ser mayor a 0"):
            AsientoConcreto(
                nombre="Test",
                material="Tela",
                color="Azul",
                precio_base=100.0,
                capacidad_personas=0
            )
    
    def test_material_tapizado_invalido(self):
        class AsientoConcreto(Asiento):
            def calcular_precio(self) -> float:
                return self.precio_base
            
            def obtener_descripcion(self) -> str:
                return "Asiento para pruebas"
        
        with pytest.raises(ValueError, match="Material tapizado debe ser uno de"):
            AsientoConcreto(
                nombre="Test",
                material="Tela",
                color="Azul",
                precio_base=100.0,
                material_tapizado="plástico"
            )
