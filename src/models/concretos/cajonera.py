"""
Clase concreta Cajonera.
Representa una cajonera genérica.
"""

from src.models.categorias.almacenamiento import Almacenamiento


class Cajonera(Almacenamiento):
    """
    Clase concreta que representa una cajonera.
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
        num_cajones: int = 3,
        tiene_ruedas: bool = False,
    ):
        """
        Constructor para cajonera.

        Args:
            nombre: Nombre de la cajonera
            material: Material de la cajonera
            color: Color de la cajonera
            precio_base: Precio base de la cajonera
            altura: Altura de la cajonera en cm
            ancho: Ancho de la cajonera en cm
            profundidad: Profundidad de la cajonera en cm
            num_compartimentos: Número de compartimentos
            num_cajones: Número de cajones
            tiene_ruedas: Si tiene ruedas o no
        """
        super().__init__(nombre, material, color, precio_base, altura, ancho, profundidad, num_compartimentos)
        self._num_cajones = num_cajones
        self._tiene_ruedas = tiene_ruedas
        
        if num_cajones <= 0:
            raise ValueError("El número de cajones debe ser mayor a 0")

    @property
    def num_cajones(self) -> int:
        """Getter para el número de cajones."""
        return self._num_cajones
        
    @num_cajones.setter
    def num_cajones(self, value: int) -> None:
        """Setter para el número de cajones con validación."""
        if value <= 0:
            raise ValueError("El número de cajones debe ser mayor a 0")
        self._num_cajones = value
        
    @property
    def tiene_ruedas(self) -> bool:
        """Getter para si tiene ruedas."""
        return self._tiene_ruedas
        
    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        """Setter para si tiene ruedas."""
        self._tiene_ruedas = value

    def calcular_precio(self) -> float:
        """Calcula el precio final de la cajonera."""
        # Usar el factor de volumen calculado en la categoría
        precio = self.precio_base * self.calcular_factor_volumen()

        # Extra por ruedas
        if self.tiene_ruedas:
            precio *= 1.1

        return precio

    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada de la cajonera.
        """
        return (
            f"Cajonera '{self.nombre}': Material={self.material}, Color={self.color}, "
            f"Dimensiones={self.altura}x{self.ancho}x{self.profundidad}cm, "
            f"Cajones={self.num_cajones}, Ruedas={'Sí' if self.tiene_ruedas else 'No'}, "
            f"Compartimentos={self.num_compartimentos}, "
            f"Precio base=${self.precio_base}"
        )
