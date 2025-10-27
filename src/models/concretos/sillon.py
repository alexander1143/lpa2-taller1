"""
Clase concreta Sillón.
Implementa un mueble de asiento para una persona, con brazos y respaldo.
"""

from src.models.categorias.asientos import Asiento


class Sillon(Asiento):
    """
    Clase concreta que representa un sillón.
    Hereda de Asiento y añade características específicas como reclinable y masajeador.
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        capacidad_personas: int = 1,
        tiene_respaldo: bool = True,
        material_tapizado: str = "tela",
        es_reclinable: bool = False,
        tiene_masajeador: bool = False
    ):
        """
        Constructor para sillón.

        Args:
            nombre: Nombre del sillón
            material: Material del sillón
            color: Color del sillón
            precio_base: Precio base del sillón
            capacidad_personas: Capacidad de personas (default 1)
            tiene_respaldo: Si tiene respaldo (default True)
            material_tapizado: Material del tapizado (tela o cuero)
            es_reclinable: Si es reclinable (default False)
            tiene_masajeador: Si tiene función de masaje (default False)
        """
        super().__init__(nombre, material, color, precio_base, capacidad_personas, tiene_respaldo, material_tapizado)
        self._es_reclinable = es_reclinable
        self._tiene_masajeador = tiene_masajeador

    @property
    def es_reclinable(self) -> bool:
        """Getter para si es reclinable."""
        return self._es_reclinable
        
    @es_reclinable.setter
    def es_reclinable(self, value: bool) -> None:
        """Setter para reclinable."""
        self._es_reclinable = value

    @property
    def tiene_masajeador(self) -> bool:
        """Getter para si tiene masajeador."""
        return self._tiene_masajeador
        
    @tiene_masajeador.setter
    def tiene_masajeador(self, value: bool) -> None:
        """Setter para masajeador."""
        self._tiene_masajeador = value

    def calcular_precio(self) -> float:
        """Calcula el precio final del sillón."""
        precio = self.precio_base
        # Factor por comodidad (heredado de Asiento)
        precio *= self.calcular_factor_comodidad()
        
        # Extras por características especiales
        if self.es_reclinable:
            precio *= 1.2  # 20% extra por ser reclinable
        if self.tiene_masajeador:
            precio *= 1.3  # 30% extra por masajeador
            
        return precio
        
    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada del sillón.
        """
        return (
            f"Sillón '{self.nombre}': Material={self.material}, Color={self.color}, "
            f"Capacidad={self.capacidad_personas} personas, "
            f"Material tapizado={self.material_tapizado or 'N/A'}, "
            f"Respaldo={'Sí' if self.tiene_respaldo else 'No'}, "
            f"Reclinable={'Sí' if self.es_reclinable else 'No'}, "
            f"Masajeador={'Sí' if self.tiene_masajeador else 'No'}, "
            f"Precio base=${self.precio_base}"
        )
