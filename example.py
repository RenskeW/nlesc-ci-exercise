import pytest
def add(a, b):
    return a + b

def subtract(a, b):
    return a + b  # do not change this line until prompted to do so.

## Tests
@pytest.mark.parametrize("test_input1, test_input2, expected", [(1, 2, 3), ("a", "b", "ab"), (-1, 3, 2)]) 
def test_add(test_input1, test_input2, expected):
    assert add(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [(5, 0, 5), (4.3, 0.9, 3.4)]) 
def test_subtract(test_input1, test_input2, expected):
    assert subtract(test_input1, test_input2) == expected