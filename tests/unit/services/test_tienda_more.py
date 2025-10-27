from unittest.mock import Mock

from src.services.tienda import TiendaMuebles
from src.models.concretos.silla import Silla


def test_obtener_estadisticas_con_mueble_falla():
    tienda = TiendaMuebles()

    # mueble que lanza excepción al calcular precio
    mueble_roto = Mock()
    mueble_roto.nombre = "MuebleRoto"
    mueble_roto.calcular_precio.side_effect = Exception("Falla precio")

    tienda.agregar_producto(mueble_roto)
    stats = tienda.obtener_estadisticas()

    # valor_inventario debe calcularse ignorando el mueble que falla
    assert isinstance(stats, dict)
    assert stats.get("valor_inventario", None) == 0


def test_vender_producto_y_acumulativos():
    tienda = TiendaMuebles()
    silla = Silla("Silla Vender", "Tela", "Gris", 100.0)

    tienda.agregar_producto(silla)
    assert len(tienda.inventario) == 1

    # vender por nombre
    resultado = tienda.vender_producto("Silla Vender")
    assert resultado is True
    assert len(tienda.inventario) == 0

    stats = tienda.obtener_estadisticas()
    # acumulativos deben reflejar la venta
    assert stats.get("total_muebles_vendidos", 0) >= 1
    assert stats.get("valor_total_ventas", 0.0) >= 0.0
