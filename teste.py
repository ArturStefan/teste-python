from bis import anobissexto
import pytest

def test_div_four_not_div_hundred():
    #Testa sé é divisivel por 4 mas não divisivel por 100
    assert 'É Bissexto' == anobissexto(1944)
    assert 'É Bissexto' != anobissexto(2018)

def test_div_four_hundred():
    #Testa se é divisivel por 400
    assert 'É Bissexto' == anobissexto(1732)
    assert 'É Bissexto' != anobissexto(1951)