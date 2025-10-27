"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

from .sofa import Sofa
from .cama import Cama


class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.

    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.

    Conceptos OOP aplicados:
    - Herencia múltiple: Hereda de Sofa y Cama
    - Resolución MRO: Maneja el orden de resolución de métodos
    - Polimorfismo: Implementa comportamientos únicos combinando funcionalidades
    - Super(): Usa super() para resolver conflictos de herencia
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        capacidad_personas: int = 3,
        material_tapizado: str = "tela",
        tamaño_cama: str = "matrimonial",
        incluye_colchon: bool = True,
        mecanismo_conversion: str = "plegable",
        tiene_respaldo: bool = True,
        tiene_brazos: bool = True,
    ):
        """
        Constructor del sofá-cama.

        Args:
            nombre (str): Nombre del mueble
            material (str): Material principal
            color (str): Color del mueble
            precio_base (float): Precio base
            capacidad_personas (int): Capacidad de personas para sentarse
            material_tapizado (str): Material del tapizado
            tamaño_cama (str): Tamaño del colchón
            incluye_colchon (bool): Si incluye colchón
            mecanismo_conversion (str): Tipo de mecanismo (plegable, extensible)
            tiene_respaldo (bool): Si tiene respaldo
            tiene_brazos (bool): Si tiene brazos
        """
        # Inicializar Sofa
        Sofa.__init__(
            self,
            nombre=nombre,
            material=material,
            color=color,
            precio_base=precio_base,
            capacidad_personas=capacidad_personas,
            tiene_respaldo=tiene_respaldo,
            material_tapizado=material_tapizado,
            tiene_brazos=tiene_brazos
        )
        
        # Inicializar Cama (con un precio base ajustado para evitar doble conteo)
        Cama.__init__(
            self,
            nombre=nombre,
            material=material,
            color=color,
            precio_base=precio_base,
            tamaño=tamaño_cama.lower(),
            incluye_colchon=incluye_colchon
        )
        
        # Atributos específicos del sofá-cama
        self._mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"

    def calcular_precio(self) -> float:
        """
        Calcula el precio final del sofá cama combinando las características de ambas clases padre.
        
        Returns:
            float: El precio final del sofá cama
        """
        # Precio base del sofá
        precio_base = self.precio_base
        
        # Factor por tamaño
        factor_tamaño = 1.0
        if self._tamaño == "matrimonial":
            factor_tamaño = 1.3  # 30% extra
        elif self._tamaño == "queen":
            factor_tamaño = 1.5  # 50% extra
        elif self._tamaño == "king":
            factor_tamaño = 1.7  # 70% extra
            
        # Factor por comodidad
        factor_comodidad = 1.0
        if self._mecanismo_conversion == "hidraulico":
            factor_comodidad = 1.2  # 20% extra
        elif self._mecanismo_conversion == "electrico":
            factor_comodidad = 1.3  # 30% extra
            
        # Factor por colchón
        factor_colchon = 1.15 if self._incluye_colchon else 1.0
            
        # Calcular precio final
        precio_final = precio_base * factor_tamaño * factor_comodidad * factor_colchon
        return round(precio_final, 2)
        
    def transformar(self) -> str:
        """
        Transforma el sofá cama entre modo sofá y modo cama.
        
        Returns:
            str: Mensaje indicando el nuevo estado
        """
        if self._modo_actual == "sofa":
            self._modo_actual = "cama"
            return "Transformado a modo cama"
        else:
            self._modo_actual = "sofa"
            return "Transformado a modo sofá"

        return round(precio_sofa, 2)

    @property
    def mecanismo_conversion(self) -> str:
        """Getter para el mecanismo de conversión."""
        return self._mecanismo_conversion

    @property
    def modo_actual(self) -> str:
        """Getter para el modo actual (sofa o cama)."""
        return self._modo_actual

    # Redefinir tamaño para compatibilidad con ambas clases
    @property
    def tamaño(self) -> str:
        """Getter para tamaño (compatible con clase Cama)."""
        return self._tamaño

    @property
    def tamaño_cama(self) -> str:
        """Alias para tamaño específico de cama."""
        return self._tamaño

    def convertir_a_cama(self) -> str:
        """
        Convierte el sofá en cama.
        Método específico del sofá-cama.

        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "cama":
            return "El sofá-cama ya está en modo cama"

        self._modo_actual = "cama"
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"

    def convertir_a_sofa(self) -> str:
        """
        Convierte la cama en sofá.
        Método específico del sofá-cama.

        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "sofa":
            return "El sofá-cama ya está en modo sofá"

        self._modo_actual = "sofa"
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
        pass

    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada del sofá cama.
        Combina información de ambas funcionalidades.
        """
        desc = f"Sofá-Cama: {self.nombre}\n"
        desc += f"  Material: {self.material}\n"
        desc += f"  Color: {self.color}\n"
        desc += f"  {self.obtener_info_asiento()}\n"
        desc += f"  Tamaño como cama: {self.tamaño_cama}\n"
        desc += f"  Incluye colchón: {'Sí' if self.incluye_colchon else 'No'}\n"
        desc += f"  Mecanismo: {self.mecanismo_conversion}\n"
        desc += f"  Modo actual: {self.modo_actual}\n"
        desc += f"  Precio final: ${self.calcular_precio()}"
        return desc

    def obtener_capacidad_total(self) -> dict:
        """
        Obtiene la capacidad tanto como sofá como cama.
        Método único del sofá-cama.

        Returns:
            dict: Capacidades en ambos modos
        """
        capacidades = {
            "como_sofa": self.capacidad_personas,
            "como_cama": 2
            if self.tamaño_cama in ["matrimonial", "queen", "king"]
            else 1,
        }
        return capacidades

    # TODO: Implementar método para verificar compatibilidad de modo
    # def puede_usar_como_cama(self) -> bool:
    #     """Verifica si actualmente puede usarse como cama."""
    #     return self._modo_actual == "cama"

    # def puede_usar_como_sofa(self) -> bool:
    #     """Verifica si actualmente puede usarse como sofá."""
    #     return self._modo_actual == "sofa"

    def __str__(self) -> str:
        """
        Representación en cadena del sofá-cama.
        Sobrescribe el método heredado para mostrar información específica.
        """
        return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"
