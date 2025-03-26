#Unit Test Exercise 1
#pip install pytest
#pytest test_hello.py
from hello import hello

def test_default():
    hello("Nico") == "hello, Nico"
    assert hello() == "hello, world"

#Unit Test Exercise 2
#pip install pytest
#pytest test_hello.py
def test_argument(): 
    assert hello("Nico") == "hello, Nico"

#Unit Test Exercise 3
#pip install pytest
#pytest test_hello.py
def test_argument1(): 
    for name in ["John", "Noel", "Erick"]:
        assert hello(name) == f"hello, {name}"

#Test Directory
#pytest dir_name