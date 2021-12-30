"""Testing invalid cookiecutter template repositories."""
import pytest

from tackle import exceptions, main


def test_should_raise_error_if_repo_does_not_exist():
    """Cookiecutter invocation with non-exist repository should raise error."""
    with pytest.raises(exceptions.UnknownSourceException):
        main.tackle('definitely-not-a-valid-repo-dir')
