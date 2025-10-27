import pytest

from src.models.concretos.mesa import Mesa
from src.models.concretos.armario import Armario
from src.models.concretos.sofa import Sofa
from src.services.tienda import TiendaMuebles


@pytest.fixture
def mesa_basica():
	return Mesa(
		nombre="Mesa Test",
		material="Madera",
		color="Café",
		precio_base=100.0,
		largo=100.0,
		ancho=60.0,
		altura=75.0,
		capacidad_personas=4,
	)


@pytest.fixture
def armario_basico():
	return Armario(
		nombre="Armario Test",
		material="Madera",
		color="Blanco",
		precio_base=200.0,
		altura=180.0,
		ancho=80.0,
		profundidad=50.0,
		num_compartimentos=2,
	)


@pytest.fixture
def sofa_basico():
	return Sofa(
		nombre="Sofa Test",
		material="Tela",
		color="Gris",
		precio_base=250.0,
		capacidad_personas=3,
		material_tapizado="tela",
	)


@pytest.fixture
def tienda_vacia():
	return TiendaMuebles()

