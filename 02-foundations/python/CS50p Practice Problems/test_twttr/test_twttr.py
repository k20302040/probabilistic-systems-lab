import twttr


def test_twttr():
    assert twttr.shorten("theitshed") == "thtshd"
    assert twttr.shorten("THEITSHED") == "THTSHD"
    assert twttr.shorten("ThEitshEd") == "Thtshd"
    assert twttr.shorten("123456") == "123456"
    assert twttr.shorten("!@#$%^") == "!@#$%^"
