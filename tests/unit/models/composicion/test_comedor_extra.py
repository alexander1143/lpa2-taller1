import pytest

from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla
from src.models.concretos.armario import Armario


def test_comedor_precio_total_y_len():
    mesa = Mesa(
        nombre="Mesa Prueba",
        material="Madera",
        color="Café",
        precio_base=200.0,
        largo=120.0,
        ancho=80.0,
        altura=75.0,
        capacidad_personas=4,
    )
    s1 = Silla("S1", "Madera", "Café", 50.0)
    s2 = Silla("S2", "Madera", "Café", 50.0)
    comedor = Comedor(nombre="Comedor Test", mesa=mesa, sillas=[s1, s2])

    assert len(comedor) == 1 + 2
    precio_esperado = mesa.calcular_precio() + s1.calcular_precio() + s2.calcular_precio()
    assert abs(comedor.calcular_precio_total() - precio_esperado) < 0.01


def test_agregar_silla_tipo_invalido_y_capacidad():
    mesa = Mesa(
        nombre="Mesa Peque",
        material="Madera",
        color="Café",
        precio_base=100.0,
        largo=50.0,
        ancho=40.0,
        altura=75.0,
        capacidad_personas=2,
    )
    comedor = Comedor(nombre="Comedor Capacidad", mesa=mesa, sillas=[])
    armario = Armario(
        nombre="No es silla",
        material="Madera",
        color="Blanco",
        precio_base=150.0,
        altura=180.0,
        ancho=80.0,
        profundidad=50.0,
    )

    # Si el comedor está vacío la comprobación de tipo no aplica (implementación actual)
    # Primero agregamos una silla válida para que exista un tipo a validar
    s_init = Silla("Init", "Madera", "Café", 40.0)
    assert comedor.agregar_silla(s_init).startswith("Silla")

    # Ahora intentar agregar un armario (tipo inválido) debe fallar
    ret = comedor.agregar_silla(armario)
    assert "Error: Solo se pueden agregar objetos de tipo Silla" in ret

    # agregar sillas hasta capacidad
    s1 = Silla("S1", "Madera", "Café", 40.0)
    s2 = Silla("S2", "Madera", "Café", 40.0)
    assert comedor.agregar_silla(s1).startswith("Silla")
    # Al intentar agregar la tercera silla en capacidad 2 debe rechazarse
    ret3 = comedor.agregar_silla(s2)
    assert "No se pueden agregar" in ret3
    # Ya en capacidad, añadir una más debe devolver mensaje de no se pueden agregar
    s3 = Silla("S3", "Madera", "Café", 40.0)
    ret2 = comedor.agregar_silla(s3)
    assert "No se pueden agregar" in ret2


def test_quitar_silla_vacia_e_indice_invalido():
    mesa = Mesa(
        nombre="Mesa Solo",
        material="Madera",
        color="Café",
        precio_base=100.0,
        largo=80.0,
        ancho=60.0,
        altura=75.0,
    )
    comedor = Comedor(nombre="Comedor Vacio", mesa=mesa, sillas=[])
    assert comedor.quitar_silla() == "No hay sillas para quitar"

    # agregar una silla y quitar con índice inválido
    s = Silla("S", "Madera", "Café", 40.0)
    comedor.agregar_silla(s)
    assert comedor.quitar_silla(10) == "Índice de silla inválido"


def test_obtener_resumen_y_materiales_unicos():
    mesa = Mesa(
        nombre="Mesa Mat",
        material="Madera",
        color="Café",
        precio_base=120.0,
        largo=120.0,
        ancho=80.0,
        altura=75.0,
    )
    s1 = Silla("S1", "Madera", "Café", 45.0, material_tapizado="tela")
    s2 = Silla("S2", "Metal", "Gris", 55.0, material_tapizado="cuero")
    comedor = Comedor(nombre="Comedor Resumen", mesa=mesa, sillas=[s1, s2])

    resumen = comedor.obtener_resumen()
    assert resumen["total_muebles"] == 1 + 2
    assert resumen["capacidad_personas"] == 2
    materiales = resumen["materiales_utilizados"]
    assert "Madera" in materiales or "madera" in [m.lower() for m in materiales]

