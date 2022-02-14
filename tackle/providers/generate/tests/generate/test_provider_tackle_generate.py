"""Tests dict input objects for `tackle.providers.tackle.generate` module."""
import pytest
import yaml
import shutil
import os

from tackle.main import tackle
from jinja2.exceptions import TemplateNotFound

FIXTURES = [
    # "file.yaml",
    # "plain-src.yaml",
    # "plain-src-block.yaml",
    # "plain-src-path.yaml",
    # "render-file.yaml",
    "render-file-additional-context.yaml",
    # "render-dir-file.yaml",
    # "render-dir-file-base.yaml",
    # "tackle-provider-remote.yaml",
]


@pytest.mark.parametrize("fixture", FIXTURES)
def test_provider_system_hook_generate_fixtures(change_dir, fixture):
    output = tackle(fixture, no_input=True)
    assert not output['init']

    if isinstance(output['after'], list):
        for i in output['after']:
            assert i
    else:
        assert output['after']


ERRORS = [
    ("missing-file.yaml", TemplateNotFound),
]


@pytest.mark.parametrize("fixture,error", ERRORS)
def test_provider_system_hook_generate_error(change_dir, fixture, error):
    with pytest.raises(error):
        tackle(fixture)


def test_provider_system_hook_copy_without_render(change_dir):
    tackle("copy-without-render.yaml")
    with open(os.path.join('output', '.hidden.yaml')) as f:
        hidden = yaml.safe_load(f)

    with open('output/no-render/dir/foo.yaml') as f:
        nested_glob = yaml.safe_load(f)

    assert hidden['stuff'] == '{{stuff}}'
    assert nested_glob['stuff'] == '{{stuff}}'
    shutil.rmtree('output')
