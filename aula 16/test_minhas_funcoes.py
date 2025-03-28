from minhas_funcoes import somar, teste

def test_somar():
    """Testa as funções somar e teste."""
    assert somar(2, 3) == 5  # Testa somar dois números positivos
    assert somar(5, 7) == 12  # Testa somar dois números positivos
    assert somar(10, -3) == 7  # Testa somar um número positivo e um negativo
    assert teste() == 6  # Testa a soma dos elementos da lista [1, 2, 3], que resulta em 6



