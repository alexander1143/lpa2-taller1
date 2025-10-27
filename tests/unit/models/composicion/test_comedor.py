import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla

class TestComedor:
    @pytest.fixture
    def comedor_basico(self):
        mesa = Mesa("Mesa Comedor", "Roble", "Roble", 200.0, "rectangular", capacidad_personas=6)
        sillas = [Silla("Silla Comedor", "Roble", "Roble", 50.0, tiene_respaldo=True) for _ in range(6)]
        return Comedor("Comedor Familiar", mesa, sillas)
    
    def test_composicion_correcta(self, comedor_basico):
        assert comedor_basico.mesa is not None
        assert len(comedor_basico.sillas) == 6
        assert isinstance(comedor_basico.mesa, Mesa)
        assert all(isinstance(silla, Silla) for silla in comedor_basico.sillas)
    
    def test_calcular_precio_total(self, comedor_basico):
        # Los precios incluyen factores de modificación (material, tamaño, etc.)
        mesa_precio = comedor_basico.mesa.calcular_precio()
        silla_precio = comedor_basico.sillas[0].calcular_precio()
        precio_esperado = mesa_precio + (6 * silla_precio)
        precio_total = comedor_basico.calcular_precio()
        assert precio_total == precio_esperado