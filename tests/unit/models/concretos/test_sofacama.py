import pytest
from src.models.concretos.sofacama import SofaCama

class TestSofaCama:
    def test_herencia_multiple(self):
        sofa_cama = SofaCama(
            nombre="Sofá Cama Moderno",
            material="Tela",
            color="Gris",
            precio_base=500.0,
            capacidad_personas=3,
            tamaño_cama="queen"
        )
        
        # Verificar atributos de Sofa
        assert sofa_cama.capacidad_personas == 3
        
        # Verificar atributos de Cama
        assert sofa_cama.tamaño == "queen"
        
        # Verificar método específico
        assert hasattr(sofa_cama, 'transformar')
    
    def test_resolucion_metodos(self):
        sofa_cama = SofaCama(
            nombre="Sofá Cama",
            material="Cuero",
            color="Marrón",
            precio_base=600.0,
            capacidad_personas=2,
            material_tapizado="cuero",
            tamaño_cama="matrimonial",
            incluye_colchon=True,
            mecanismo_conversion="electrico"
        )
        
        # Verificar que usa el método correcto (MRO)
        precio = sofa_cama.calcular_precio()
        # Precio base * 1.3 (tamaño matrimonial) * 1.3 (mecanismo eléctrico) * 1.15 (colchón)
        precio_esperado = 600.0 * 1.3 * 1.3 * 1.15
        assert abs(precio - precio_esperado) < 0.01  # Aproximadamente 1166.1