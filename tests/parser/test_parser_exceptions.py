"""Test the input source part of the parser."""
import pytest

from tackle.exceptions import EmptyTackleFileException
from tackle.cli import main

INPUT_SOURCES = [
    ("empty.yaml", EmptyTackleFileException),
    # ("")
]


@pytest.mark.parametrize("input_file,exception", INPUT_SOURCES)
def test_parser_raises_exceptions(change_curdir_fixtures, input_file, exception):
    """Test raising exceptions."""
    with pytest.raises(exception):
        main([input_file])
