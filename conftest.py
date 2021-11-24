"""pytest fixtures which are globally available throughout the suite."""
import os
import oyaml as yaml
from click.testing import CliRunner
from tackle.__main__ import main

import pytest


@pytest.fixture(scope="function")
def change_dir(request):
    """Change to the current directory of the test."""
    os.chdir(request.fspath.dirname)


@pytest.fixture(scope='function')
def change_curdir_fixtures(request):
    """Change to the fixtures dir in the current directory of the test."""
    os.chdir(os.path.join(request.fspath.dirname, 'fixtures'))


@pytest.fixture(scope='function')
def change_dir_base(monkeypatch):
    """Change to the current directory."""
    monkeypatch.chdir(os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture(scope='function')
def change_dir_main_fixtures(request):
    """Change to the current directory."""
    os.chdir(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)), 'tests', 'main', 'fixtures'
        )
    )


@pytest.fixture(scope='session')
def cli_runner():
    """Fixture that returns a helper function to run the cookiecutter cli."""
    runner = CliRunner()

    def cli_main(*cli_args, **cli_kwargs):
        """Run tackle cli main with the given args."""
        return runner.invoke(main, cli_args, **cli_kwargs)

    return cli_main
