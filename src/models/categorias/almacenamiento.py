"""
Clase abstracta para muebles de almacenamiento.
"""

from abc import ABC, abstractmethod
from models.mueble import Mueble


class Almacenamiento(Mueble, ABC):
    """
    Clase abstracta para muebles de almacenamiento (como armarios, cajoneras, etc).
    Hereda de Mueble y define la interfaz base para este tipo de muebles.

    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Define características comunes de almacenamiento
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        altura: float,
        ancho: float,
        profundidad: float,
        num_compartimentos: int = 1,
    ):
        """
        Constructor para muebles de almacenamiento.

        Args:
            altura: Altura del mueble en cm
            ancho: Ancho del mueble en cm
            profundidad: Profundidad del mueble en cm
            num_compartimentos: Número de compartimentos/divisiones

        Raises:
            ValueError: Si alguna dimensión es menor o igual a 0
            ValueError: Si el número de compartimentos es menor o igual a 0
        """
        if altura <= 0:
            raise ValueError("La altura debe ser mayor a 0")
        if ancho <= 0:  
            raise ValueError("El ancho debe ser mayor a 0")
        if profundidad <= 0:
            raise ValueError("La profundidad debe ser mayor a 0")
        if num_compartimentos <= 0:
            raise ValueError("El número de compartimentos debe ser mayor o igual a 0")

        super().__init__(nombre, material, color, precio_base)
        self._altura = altura
        self._ancho = ancho 
        self._profundidad = profundidad
        self._num_compartimentos = num_compartimentos

    @property
    def num_compartimentos(self) -> int:
        """Getter para número de compartimentos."""
        return self._num_compartimentos

    @num_compartimentos.setter
    def num_compartimentos(self, value: int) -> None:
        """Setter para compartimentos con validación."""
        if value <= 0:
            raise ValueError("El número de compartimentos debe ser mayor a 0")
        self._num_compartimentos = value

    @property
    def altura(self) -> float:
        """Getter para la altura del mueble."""
        return self._altura

    @altura.setter
    def altura(self, value: float) -> None:
        """Setter para altura con validación."""
        if value <= 0:
            raise ValueError("La altura debe ser mayor a 0")
        self._altura = value

    @property
    def ancho(self) -> float:
        """Getter para el ancho del mueble."""
        return self._ancho

    @ancho.setter
    def ancho(self, value: float) -> None:
        """Setter para ancho con validación."""
        if value <= 0:
            raise ValueError("El ancho debe ser mayor a 0")
        self._ancho = value

    @property
    def profundidad(self) -> float:
        """Getter para la profundidad del mueble."""
        return self._profundidad

    @profundidad.setter
    def profundidad(self, value: float) -> None:
        """Setter para profundidad con validación."""
        if value <= 0:
            raise ValueError("La profundidad debe ser mayor a 0")
        self._profundidad = value

    def calcular_volumen(self) -> float:
        """
        Calcula el volumen del mueble en cm³.

        Returns:
            float: Volumen en centímetros cúbicos
        """
        return self.altura * self.ancho * self.profundidad

    def calcular_factor_volumen(self) -> float:
        """
        Calcula el factor de precio basado en el volumen.
        A mayor volumen, mayor precio base.

        Returns:
            float: Factor multiplicador por volumen 
            Factor base 1.0 + 0.1 por cada 100000 cm³
        """
        volumen = self.calcular_volumen()
        return 1.0 + (volumen / 100000) * 0.1

    def calcular_factor_almacenamiento(self) -> float:
        """
        Calcula un factor basado en la capacidad de almacenamiento.

        Returns:
            float: Factor multiplicador para el precio
        """
        factor = 1.0
        # Más compartimentos = más funcionalidad
        factor += (self.num_compartimentos - 1) * 0.05
        # Factor por volumen
        factor *= self.calcular_factor_volumen()
        return factor

    def obtener_info_almacenamiento(self) -> str:
        """
        Obtiene información específica del almacenamiento.

        Returns:
            str: Información detallada del almacenamiento
        """
        return f"Compartimentos: {self.num_compartimentos}, Capacidad: {self.capacidad_litros}L"

    @abstractmethod
    def calcular_precio(self) -> float:
        """Método abstracto para calcular precio."""
        pass

    @abstractmethod
    def obtener_descripcion(self) -> str:
        """Método abstracto para obtener descripción."""
        pass
