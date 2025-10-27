"""
Clase abstracta para muebles de asiento.
Esta clase agrupa las características comunes de sillas, sillones y sofás.
"""

from abc import ABC, abstractmethod
from models.mueble import Mueble


class Asiento(Mueble, ABC):
    """
    Clase abstracta para todos los muebles donde las personas se sientan.

    Hereda de Mueble y añade características específicas de los asientos
    como capacidad de personas, tipo de respaldo, etc.

    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de asientos
    - Polimorfismo: Permite diferentes implementaciones del cálculo de comodidad
    """

    MATERIALES_TAPIZADO_VALIDOS = ["tela", "cuero"]

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        capacidad_personas: int = 1,
        tiene_respaldo: bool = False,
        material_tapizado: str = None,
    ):
        """
        Constructor para muebles de asiento.

        Args:
            capacidad_personas: Número de personas que pueden sentarse
            tiene_respaldo: Si el asiento tiene respaldo o no
            material_tapizado: Material del tapizado (opcional)
            Otros argumentos heredados de Mueble

        Raises:
            ValueError: Si la capacidad es menor o igual a 0
            ValueError: Si el material de tapizado no es válido
        """
        if capacidad_personas <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        
        if material_tapizado and material_tapizado.lower() not in self.MATERIALES_TAPIZADO_VALIDOS:
            raise ValueError(f"Material tapizado debe ser uno de {self.MATERIALES_TAPIZADO_VALIDOS}")

        super().__init__(nombre, material, color, precio_base)

        self._capacidad_personas = capacidad_personas
        self._tiene_respaldo = tiene_respaldo
        self._material_tapizado = material_tapizado.lower() if material_tapizado else None

    @property
    def capacidad_personas(self) -> int:
        """Getter para la capacidad de personas."""
        return self._capacidad_personas

    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        """Setter para capacidad con validación."""
        if value <= 0:
            raise ValueError("La capacidad debe ser mayor a 0")
        self._capacidad_personas = value

    @property
    def tiene_respaldo(self) -> bool:
        """Getter para si tiene respaldo."""
        return self._tiene_respaldo

    @tiene_respaldo.setter
    def tiene_respaldo(self, value: bool) -> None:
        """Setter para respaldo."""
        self._tiene_respaldo = value

    @property
    def material_tapizado(self) -> str:
        """Getter para el material de tapizado."""
        return self._material_tapizado

    @material_tapizado.setter
    def material_tapizado(self, value: str) -> None:
        """Setter para material de tapizado."""
        self._material_tapizado = value

    def calcular_factor_comodidad(self) -> float:
        """
        Calcula un factor de comodidad basado en las características del asiento.
        Este es un método concreto que pueden usar las clases hijas.

        Returns:
            float: Factor multiplicador para el precio (1.0 = neutral)
                  +0.1 por respaldo
                  +0.1 por material tela
                  +0.2 por material cuero
        """
        factor = 1.0

        # Factor por respaldo
        if self.tiene_respaldo:
            factor += 0.1

        # Factor por material de tapizado
        if self.material_tapizado:
            if self.material_tapizado.lower() == "cuero":
                factor += 0.2
            elif self.material_tapizado.lower() == "tela":
                factor += 0.1

        # Redondear a 2 decimales para evitar pequeñas imprecisiones flotantes
        return round(factor, 2)

    def obtener_info_asiento(self) -> str:
        """
        Obtiene información específica del asiento.
        Método concreto auxiliar para las clases hijas.

        Returns:
            str: Información detallada del asiento
        """
        info = f"Capacidad: {self.capacidad_personas} personas"
        info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        if self.material_tapizado:
            info += f", Tapizado: {self.material_tapizado}"
        return info

    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Método abstracto para calcular el precio del asiento.
        Cada clase concreta debe implementar su propio cálculo.
        """
        pass

    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Método abstracto para obtener la descripción del asiento.
        Cada clase concreta debe implementar su propia descripción.
        """
        pass
