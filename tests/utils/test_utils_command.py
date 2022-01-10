"""Test for tackle.utils.command"""
import pytest

from tackle.utils.command import unpack_args_kwargs_string, unpack_input_string

TEMPLATES = [
    ('foo bar baz', 3, 0, 0),
    ('foo --bar baz bing', 2, 1, 0),
    ('foo bar --baz foo', 2, 1, 0),
    ('foo bar --baz foo --bing baz', 2, 2, 0),
    ('foo --bar baz', 1, 1, 0),
    ('foo bar --baz', 2, 0, 1),
    ('foo bar baz --bing', 3, 0, 1),
    ('foo --bar baz --foo', 1, 1, 1),
    ('foo bar --foo bar --bing --baz bling', 2, 2, 1),
    ('foo --bar baz blah --bling', 2, 1, 1),
    ('this --if "expanded == \'that\'"', 1, 1, 0),
    # These should all have `var` prepended to the args as it is indicative of a render
    ('"{{foo}}" bar baz', 4, 0, 0),
    ('{{ foo }} bar baz', 4, 0, 0),
    ('{{ foo }} bar baz bing', 5, 0, 0),
    ('{{ foo}} bar baz', 4, 0, 0),
    ('{{foo }} bar baz', 4, 0, 0),
    ('{{ foo }}-foo bar baz', 4, 0, 0),
    ('bar-{{ foo }}-foo', 2, 0, 0),
    ('bar-{{ foo in var }}-foo', 2, 0, 0),
]


@pytest.mark.parametrize("template,len_args,len_kwargs,len_flags", TEMPLATES)
def test_unpack_args_kwargs(template, len_args, len_kwargs, len_flags):
    """Validate the count of each input arg/kwarg/flag."""
    args, kwargs, flags = unpack_input_string(template)

    assert len_args == len(args)
    assert len_kwargs == len(kwargs)
    assert len_flags == len(flags)


FIXTURES = [
    # input_string, args, kwargs, flags
    ("this --if \"expanded == 'that'\"", ["this"], {"if": "expanded == 'that'"}, []),
    (
        "this that --if \"expanded == 'that'\"",
        ["this", "that"],
        {"if": "expanded == 'that'"},
        [],
    ),
]


@pytest.mark.parametrize("input_string,args,kwargs,flags", FIXTURES)
def test_unpack_input_string(input_string, args, kwargs, flags):
    """Validate expressions for input strings."""
    args_out, kwargs_out, flags_out = unpack_args_kwargs_string(input_string)
    assert args_out == args
    assert kwargs_out == kwargs
    assert flags_out == flags
