"""Application entrypoint."""


def increase(number: int, by: int = 1) -> int:
    """Dummy function to test project setup.

    >>> [increase(0, by=value) for value in range(6)]
    [1, 2, 3, 4, 5, 7]

    Args:
        number: Number that should be increased.
        by: Value by which number should be increased.

    Returns:
        Number increased by given value.

    """
    return number + by
