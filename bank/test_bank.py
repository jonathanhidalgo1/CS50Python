from bank import value


def test_hello():
    assert value("hello") == "$0"


def test_start_h():
    assert value("hi") == "$20"


def test_start_any():
    assert value("whats goin on") == "$100"
