"""
Clase concreta Cama.
Representa una cama genérica.
"""

from ..mueble import Mueble
class Cama(Mueble):
    """
    Clase concreta que representa una cama.
    """

    # Factores de precio por tamaño
    FACTORES_TAMAÑO = {
        "individual": 1.0,
        "matrimonial": 1.3,
        "queen": 1.5,
        "king": 1.7,
    }

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        tamaño: str = "individual",
        incluye_colchon: bool = False,
        tiene_cabecera: bool = False,
    ):
        """
        Inicializa una instancia de Cama.
        """
        if tamaño not in self.FACTORES_TAMAÑO:
            raise ValueError(f"Tamaño debe ser uno de: {list(self.FACTORES_TAMAÑO.keys())}")

        super().__init__(nombre, material, color, precio_base)
        self._tamaño = tamaño
        self._incluye_colchon = incluye_colchon
        self._tiene_cabecera = tiene_cabecera

    @property
    def tamaño(self) -> str:
        return self._tamaño

    @tamaño.setter
    def tamaño(self, value: str) -> None:
        if value not in self.FACTORES_TAMAÑO:
            raise ValueError(f"Tamaño debe ser uno de: {list(self.FACTORES_TAMAÑO.keys())}")
        self._tamaño = value

    @property
    def incluye_colchon(self) -> bool:
        return self._incluye_colchon

    @property
    def tiene_cabecera(self) -> bool:
        return self._tiene_cabecera

    def calcular_precio(self) -> float:
        precio = self.precio_base
        precio *= self.FACTORES_TAMAÑO[self.tamaño]
        if self.incluye_colchon:
            precio *= 1.15
        if self.tiene_cabecera:
            precio *= 1.1
        return precio

    def obtener_descripcion(self) -> str:
        desc = f"Cama: {self.nombre}\n"
        desc += f"  Material: {self.material}\n"
        desc += f"  Color: {self.color}\n"
        desc += f"  Tamaño: {self.tamaño}\n"
        desc += f"  Incluye colchón: {'Sí' if self.incluye_colchon else 'No'}\n"
        desc += f"  Cabecera: {'Sí' if self.tiene_cabecera else 'No'}\n"
        desc += f"  Precio final: ${self.calcular_precio()}"
        return desc
