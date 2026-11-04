from tools import parse_port, percent


def test_parse_port_valid():
    assert parse_port("8080") == 8080


def test_parse_port_invalid():
    assert parse_port("abc") == 0


def test_percent():
    assert percent(1, 2) == 50