from Testing_01 import suma, is_mayor

def test_sum():
    assert suma(2, 3) == 5
    assert suma(0, 0) == 0
    assert suma(-5, 5) == 0

def test_is_mayor():
    assert is_mayor(5, 3) == True
    assert is_mayor(3, 5) == False
    

test_sum()
test_is_mayor()
