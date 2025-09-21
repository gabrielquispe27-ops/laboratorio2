from mypackage.calculator import add

def test_add_positive():
    """Prueba la suma de dos números positivos."""
    assert add(2, 3) == 5

def test_add_negative():
    """Prueba la suma de dos números negativos."""
    assert add(-1, -4) == -5

def test_add_positive_and_negative():
    """Prueba la suma de un número positivo y uno negativo."""
    assert add(10, -5) == 5