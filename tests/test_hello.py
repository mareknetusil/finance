from finance.hello import main, add

def test_hello() -> None:
    main()


def test_add() -> None:
    assert add(1, 2) == 3
