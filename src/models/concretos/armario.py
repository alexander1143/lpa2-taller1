"""
Clase concreta Armario.
Representa un armario genérico.
"""

from src.models.categorias.almacenamiento import Almacenamiento


class Armario(Almacenamiento):
    """
    Clase concreta que representa un armario.
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
        num_compartimentos: int = 2,
        num_puertas: int = 2,
        tipo_puertas: str = "batientes"
    ):
        """
        Constructor para armario.

        Args:
            nombre: Nombre del armario
            material: Material del armario
            color: Color del armario
            precio_base: Precio base del armario
            altura: Altura del armario en cm
            ancho: Ancho del armario en cm
            profundidad: Profundidad del armario en cm
            num_compartimentos: Número de compartimentos
            num_puertas: Número de puertas
            tipo_puertas: Tipo de puertas (batientes o corredizas)
        """
        super().__init__(nombre, material, color, precio_base, altura, ancho, profundidad, num_compartimentos)
        self._num_puertas = num_puertas
        self._tipo_puertas = tipo_puertas
        
        if tipo_puertas not in ["batientes", "corredizas"]:
            raise ValueError("Tipo de puertas debe ser uno de: batientes, corredizas")
        if num_puertas <= 0:
            raise ValueError("El número de puertas debe ser mayor a 0")

    @property
    def num_puertas(self) -> int:
        """Getter para el número de puertas."""
        return self._num_puertas

    @num_puertas.setter
    def num_puertas(self, value: int) -> None:
        """Setter para el número de puertas con validación."""
        if value <= 0:
            raise ValueError("El número de puertas debe ser mayor a 0")
        self._num_puertas = value

    @property
    def tipo_puertas(self) -> str:
        """Getter para el tipo de puertas."""
        return self._tipo_puertas

    @tipo_puertas.setter
    def tipo_puertas(self, value: str) -> None:
        """Setter para el tipo de puertas con validación."""
        if value not in ["batientes", "corredizas"]:
            raise ValueError("Tipo de puertas debe ser uno de: batientes, corredizas")
        self._tipo_puertas = value

    def calcular_precio(self) -> float:
        """Calcula el precio final del armario."""
        # Usar el factor provisto por la categoría Almacenamiento
        precio = self.precio_base * self.calcular_factor_volumen()

        # Extra por tipo de puertas (corredizas)
        if self.tipo_puertas == "corredizas":
            precio *= 1.15

        return precio

    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada del armario.
        """
        return (
            f"Armario '{self.nombre}': Material={self.material}, Color={self.color}, "
            f"Dimensiones={self.altura}x{self.ancho}x{self.profundidad}cm, "
            f"Puertas={self.num_puertas} ({self.tipo_puertas}), "
            f"Compartimentos={self.num_compartimentos}, "
            f"Precio base=${self.precio_base}"
        )
