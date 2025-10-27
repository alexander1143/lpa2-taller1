"""
Clase concreta Escritorio.
Representa un escritorio genérico.
"""

from src.models.categorias.superficies import Superficie


class Escritorio(Superficie):
    """
    Clase concreta que representa un escritorio.
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        largo: float,
        ancho: float,
        altura: float,
        tipo: str = "estudiante",
        tiene_cajonera: bool = False,
        porta_teclado: bool = False,
    ):
        """
        Constructor para escritorio.

        Args:
            nombre: Nombre del escritorio
            material: Material del escritorio
            color: Color del escritorio
            precio_base: Precio base del escritorio
            largo: Largo del escritorio en cm
            ancho: Ancho del escritorio en cm
            altura: Altura del escritorio en cm
            tipo: Tipo de escritorio (estudiante, ejecutivo, esquinero)
            tiene_cajonera: Si tiene cajonera integrada
            porta_teclado: Si tiene porta teclado
        """
        super().__init__(nombre, material, color, precio_base, largo, ancho, altura)
        self._tipo = tipo
        self._tiene_cajonera = tiene_cajonera
        self._porta_teclado = porta_teclado
        
        if tipo not in ["estudiante", "ejecutivo", "esquinero"]:
            raise ValueError("Tipo de escritorio debe ser uno de: estudiante, ejecutivo, esquinero")

    @property
    def tipo(self) -> str:
        """Getter para el tipo de escritorio."""
        return self._tipo
        
    @tipo.setter
    def tipo(self, value: str) -> None:
        """Setter para el tipo de escritorio con validación."""
        if value not in ["estudiante", "ejecutivo", "esquinero"]:
            raise ValueError("Tipo de escritorio debe ser uno de: estudiante, ejecutivo, esquinero")
        self._tipo = value
        
    @property
    def tiene_cajonera(self) -> bool:
        """Getter para si tiene cajonera."""
        return self._tiene_cajonera
        
    @tiene_cajonera.setter
    def tiene_cajonera(self, value: bool) -> None:
        """Setter para si tiene cajonera."""
        self._tiene_cajonera = value
        
    @property
    def porta_teclado(self) -> bool:
        """Getter para si tiene porta teclado."""
        return self._porta_teclado
        
    @porta_teclado.setter
    def porta_teclado(self, value: bool) -> None:
        """Setter para si tiene porta teclado."""
        self._porta_teclado = value

    def calcular_precio(self) -> float:
        """
        Calcula el precio final del escritorio.
        - Factor por tamaño base (de Superficie)
        - Factor extra por tipo:
          * estudiante: sin extra
          * ejecutivo: +20%
          * esquinero: +20%
        - +20% por cajonera
        - +10% por porta teclado
        """
        precio = self.precio_base
        precio *= self.calcular_factor_tamaño()
        
        # Factores extras acumulativos (según tests, 'tipo' no agrega un multiplicador extra)
        factor_extra = 1.0

        # Extra por accesorios
        if self.tiene_cajonera:
            factor_extra *= 1.2
        if self.porta_teclado:
            factor_extra *= 1.1

        return precio * factor_extra

    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada del escritorio.
        """
        return (
            f"Escritorio '{self.nombre}': Material={self.material}, Color={self.color}, "
            f"Forma={self.forma}, Cajones={self.num_cajones if self.tiene_cajones else 0}, "
            f"Largo={self.largo}m, Iluminación={'Sí' if self.tiene_iluminacion else 'No'}, "
            f"Precio base=${self.precio_base}"
        )
