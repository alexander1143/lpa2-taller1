import pytest
from src.models.categorias.almacenamiento import Almacenamiento

class TestAlmacenamiento:
    @pytest.fixture
    def almacenamiento_basico(self):
        class AlmacenamientoConcreto(Almacenamiento):
            def calcular_precio(self) -> float:
                return self.precio_base * self.calcular_factor_volumen()
            
            def obtener_descripcion(self) -> str:
                return f"Mueble de almacenamiento para pruebas"
        
        return AlmacenamientoConcreto(
            nombre="Almacenamiento Test",
            material="Madera",
            color="Café",
            precio_base=100.0,
            altura=100.0,
            ancho=50.0,
            profundidad=40.0,
            num_compartimentos=2
        )
    
    def test_inicializacion(self, almacenamiento_basico):
        assert almacenamiento_basico.altura == 100.0
        assert almacenamiento_basico.ancho == 50.0
        assert almacenamiento_basico.profundidad == 40.0
        assert almacenamiento_basico.num_compartimentos == 2
    
    def test_calcular_volumen(self, almacenamiento_basico):
        volumen = almacenamiento_basico.calcular_volumen()
        assert volumen == 100.0 * 50.0 * 40.0  # altura * ancho * profundidad
    
    def test_calcular_factor_volumen(self, almacenamiento_basico):
        factor = almacenamiento_basico.calcular_factor_volumen()
        volumen = almacenamiento_basico.calcular_volumen()
        # Factor base 1.0 + 0.1 por cada 100000 cm³
        factor_esperado = 1.0 + (volumen / 100000) * 0.1
        assert abs(factor - factor_esperado) < 0.01
    
    def test_validacion_dimensiones(self):
        class AlmacenamientoConcreto(Almacenamiento):
            def calcular_precio(self) -> float:
                return self.precio_base
            
            def obtener_descripcion(self) -> str:
                return "Mueble de almacenamiento para pruebas"
        
        with pytest.raises(ValueError, match="debe ser mayor a 0"):
            AlmacenamientoConcreto(
                nombre="Test",
                material="Madera",
                color="Café",
                precio_base=100.0,
                altura=-1,
                ancho=50.0,
                profundidad=40.0
            )
    
    def test_validacion_compartimentos(self):
        class AlmacenamientoConcreto(Almacenamiento):
            def calcular_precio(self) -> float:
                return self.precio_base
            
            def obtener_descripcion(self) -> str:
                return "Mueble de almacenamiento para pruebas"
        
        with pytest.raises(ValueError, match="debe ser mayor o igual a 0"):
            AlmacenamientoConcreto(
                nombre="Test",
                material="Madera",
                color="Café",
                precio_base=100.0,
                altura=100.0,
                ancho=50.0,
                profundidad=40.0,
                num_compartimentos=-1
            )
