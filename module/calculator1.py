#Calculator Exercise 1 Unit Test
import pytest
from calculator import square

def main():
    test_square()
    test_square1()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
            print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
         print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
         print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
         print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
         print("0 squared was not 0")
    
if __name__ == "__main__":
    main()

#Calculator Exercise 2 Unit Test
#pip install pytest
#pytest calculator1.py
from calculator import square

def test_square1():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

from calculator import square
def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
     assert square(-2) == 4
     assert square(-3) == 9

def test_zero():
     assert square(0) == 0

#Calculator Exercise 3 Unit Test
#pip install pytest
#change x = int("What's x?" ) in calulator.py
#pytest calculator1.py
def test_str():
     with pytest.raises(TypeError):
        square("Cat")