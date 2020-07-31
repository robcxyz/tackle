# -*- coding: utf-8 -*-

"""Tests dict input objects for `cookiecutter.operator.block` module."""
import os
from cookiecutter.main import cookiecutter


def test_operator_dict(monkeypatch, tmpdir):
    """Verify the operator call works successfully."""
    monkeypatch.chdir(os.path.abspath(os.path.dirname(__file__)))

    output = cookiecutter(
        '.', context_file='merge.yaml', no_input=True, output_dir=str(tmpdir)
    )
    assert output

    output = cookiecutter(
        '.', context_file='update.yaml', no_input=True, output_dir=str(tmpdir)
    )
    assert output
