# -*- coding: utf-8 -*-

"""Tests dict input objects for `cookiecutter.parser.providers` module."""
import os

import pytest
from tackle.main import tackle
import subprocess
import sys


@pytest.fixture()
def temporary_uninstall(package='art'):
    """Fixture to uninstall a package and install it after the test."""
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "uninstall",
            "--quiet",
            "--disable-pip-version-check",
            "-y",
            package,
        ]
    )
    yield


def test_parser_provider_import_installs_requirements(
    change_curdir_fixtures, temporary_uninstall
):
    """Validate that if a package is missing, that it will be installed and usable."""
    tackle('text2art.yaml')


def test_parser_hooks_raises_error_on_unknown_hook_type(change_curdir_fixtures):
    """Verify raising error.

    Verify that the hook parser raises the right error when the hook type is
    not in the providers.
    """
    from tackle.exceptions import UnknownHookTypeException

    with pytest.raises(UnknownHookTypeException):
        tackle('unknown-hook-type.yaml')


def test_parser_provider_hook_add(change_curdir_fixtures):
    """Validate adding providers.

    Validate that you can give a `__provider` key to point to
    additional providers and make them available as a type.
    """
    os.chdir('test-provider')
    o = tackle('context_provider.yaml')
    assert o['things'] == 'bar'


def test_parser_provider_hook_add_list(change_curdir_fixtures):
    """Validate adding providers.

    Validate that you can give multiple `__provider` keys to point to
    additional providers and make them available as a types.
    """
    o = tackle('context_provider_list.yaml')
    assert o['things'] == 'bar'
    assert o['stuff'] == 'bar'
