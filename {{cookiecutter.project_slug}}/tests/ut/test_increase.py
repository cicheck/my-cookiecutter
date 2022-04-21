import pytest

from {{cookiecutter.project_slug}}.__main__ import increase


@pytest.mark.parametrize("by", [0, 1, 2, 3, 4, 5, 6])  # type: ignore[misc]
def test_increase(by: int) -> None:
    assert increase(0, by) == by
