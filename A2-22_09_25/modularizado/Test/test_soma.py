import pytest
from modularizado.calculadora import soma

def test_soma_positivos():
		assert soma(3, 5) == 8

def test_soma_negativos():
		assert soma(-3, -5) == -8

def test_soma_zero():
		assert soma(0, 5) == 5
		assert soma(3, 0) == 3
		assert soma(0, 0) == 0

def test_soma_maior_que_zero():
		assert soma(3, 5) > 0

def test_soma_nao_negativo():
		assert not soma(-3, -5) < 0
