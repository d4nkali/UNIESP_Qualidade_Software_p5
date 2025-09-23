import pytest
from modularizado.calculadora import multiplicacao

def test_multiplicacao_positivos():
		assert multiplicacao(3, 5) == 15

def test_multiplicacao_negativos():
		assert multiplicacao(-3, -5) == 15

def test_multiplicacao_zero():
		assert multiplicacao(0, 5) == 0
		assert multiplicacao(3, 0) == 0
		assert multiplicacao(0, 0) == 0

def test_multiplicacao_maior_que_zero():
		assert multiplicacao(3, 5) > 0

def test_multiplicacao_nao_negativo():
		assert not multiplicacao(-3, -5) < 0
