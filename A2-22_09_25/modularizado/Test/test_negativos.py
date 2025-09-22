import pytest
from modularizado.calculadora import subtracao

def test_subtracao_positivos():
    assert subtracao(10, 5) == 5

def test_subtracao_negativos():
    assert subtracao(-10, -5) == -5

def test_subtracao_zero():
		assert subtracao(0, 5) == -5
		assert subtracao(5, 0) == 5
		assert subtracao(0, 0) == 0
