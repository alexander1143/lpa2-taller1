from src.models.concretos.mesa import Mesa


def test_tienda_agregar_y_buscar_por_inventario(tienda_vacia):
    tienda = tienda_vacia
    mesa = Mesa(
        nombre="Mesa Venta",
        material="Madera",
        color="Café",
        precio_base=150.0,
        largo=120.0,
        ancho=80.0,
        altura=75.0,
        capacidad_personas=4,
    )

    tienda.agregar_producto(mesa)
    assert any(p.nombre == "Mesa Venta" for p in tienda.inventario)


def test_tienda_vender_producto_por_nombre(tienda_vacia):
    tienda = tienda_vacia
    mesa = Mesa(
        nombre="Mesa a Eliminar",
        material="Madera",
        color="Café",
        precio_base=120.0,
        largo=100.0,
        ancho=70.0,
        altura=75.0,
        capacidad_personas=4,
    )
    tienda.agregar_producto(mesa)
    assert len(tienda.inventario) == 1
    vendido = tienda.vender_producto("Mesa a Eliminar")
    assert vendido is True
    assert len(tienda.inventario) == 0
