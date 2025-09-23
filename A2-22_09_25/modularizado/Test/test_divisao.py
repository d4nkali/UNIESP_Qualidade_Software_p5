import pytest
from modularizado.calculadora import divisao

def test_divisao_positivos():
    assert divisao(4, 2) == 2
    
def test_divisao_negativos():
		assert divisao(-4, -2) == 2

def test_divisao_zero():
		assert divisao(0, 5) == 0
		assert divisao(0, -5) == 0

def  test_divisao_por_zero():
		with pytest.raises(ZeroDivisionError):
				divisao(5, 0)

def test_divisao_maior_que_zero():
		assert divisao(4, 2) > 0

def test_divisao_nao_negativo():
		assert not divisao(-4, -2) < 0
