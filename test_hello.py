from hello2 import hello

def test_hello():
    assert hello("David") == "hello, David"
def test_world():
    assert hello() == "hello, world"
