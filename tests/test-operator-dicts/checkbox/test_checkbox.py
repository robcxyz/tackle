# -*- coding: utf-8 -*-

"""Tests dict input objects for `cookiecutter.prompt` module."""

import pytest
import yaml

from cookiecutter import prompt

from cookiecutter.operator import run_operator
from cookiecutter.main import cookiecutter

from helpers import create_example_fixture, keys

from pprint import pprint

FIXTURES = ['checkbox_bad.yaml']

example_app = create_example_fixture('./checkbox.py')


def test_checkbox(example_app):
    example_app.write(keys.ENTER)
    # example_app.write(keys.ENTER)
    # example_app.write(keys.ENTER)
    # example_app.write(keys.ENTER)


# class TestPromptHookDicts(object):
#     """Class to test all the dict input objects."""
#
#     @pytest.mark.parametrize("input_dicts,invalid", FIXTURES)
#     def test_hook_checkbox(self, monkeypatch):
#         """Verify `prompt_for_config` call `read_user_variable` on dict request."""
#
#         monkeypatch.setattr(
#             'cookiecutter.prompt.read_user_dict',
#             lambda var, default: {"key": "value", "integer": 37},
#         )
#         context = {'cookiecutter': {'details': {}}}
#
#         cookiecutter_dict = prompt.prompt_for_config(context)
#         assert cookiecutter_dict == {'details': {'key': u'value', 'integer': 37}}
