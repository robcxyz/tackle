"""Tests for all supported cookiecutter template repository locations."""
import pytest

from tackle.models import DEFAULT_ABBREVIATIONS
from tackle.utils.paths import expand_abbreviations, is_repo_url


@pytest.fixture(
    params=[
        'gitolite@server:team/repo',
        'git@github.com:audreyr/cookiecutter.git',
        'https://github.com/audreyr/cookiecutter.git',
        'git+https://private.com/gitrepo',
        'hg+https://private.com/mercurialrepo',
        'https://bitbucket.org/pokoli/cookiecutter.hg',
        'file://server/path/to/repo.git',
    ]
)
def remote_repo_url(request):
    """Fixture. Represent possible URI to different repositories types."""
    return request.param


def test_is_repo_url_for_remote_urls(remote_repo_url):
    """Verify is_repo_url works."""
    assert is_repo_url(remote_repo_url) is True


@pytest.fixture(
    params=[
        '/audreyr/cookiecutter.git',
        '/home/audreyr/cookiecutter',
        (
            'c:\\users\\foo\\appdata\\local\\temp\\1\\pytest-0\\'
            'test_default_output_dir0\\template'
        ),
    ]
)
def local_repo_url(request):
    """Fixture. Represent possible paths to local resources."""
    return request.param


def test_is_repo_url_for_local_urls(local_repo_url):
    """Verify is_repo_url works."""
    assert is_repo_url(local_repo_url) is False


def test_expand_abbreviations():
    """Validate `repository.expand_abbreviations` correctly translate url."""
    template = 'gh:audreyr/cookiecutter-pypackage'

    # This is not a valid repo url just yet!
    # First `repository.expand_abbreviations` needs to translate it
    assert is_repo_url(template) is False

    expanded_template = expand_abbreviations(template, DEFAULT_ABBREVIATIONS)
    assert is_repo_url(expanded_template) is True
