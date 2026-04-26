from bank import value

def test_value1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("    hello  ") == 0
def test_value2():
    assert value("hi") == 20
    assert value("hlak") == 20
    assert value("    Helo  ") == 20
def test_value3() :
    assert value("cs50") == 100
    assert value("50") == 100
    assert value("    what's up?  ") == 100
