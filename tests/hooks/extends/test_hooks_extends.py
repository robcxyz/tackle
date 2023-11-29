from tackle import tackle


def test_hooks_extends_str():
    """Check that we can extend a base function."""
    output = tackle('extends.yaml')
    assert output['t'] == ['hello', 'world']


def test_hooks_extends_list():
    """Check that we can extend a base hook with a list of other hooks."""
    output = tackle('extends-list.yaml')
    assert output['t'] == ['hello', 'dude']


def test_hooks_extends_method():
    """Check that we can extend a method from a base hook."""
    output = tackle('extends-method.yaml')
    assert output['t']


def test_hooks_extends_python_hook(cd):
    """Check that we can extend a python hook."""
    cd('python-extend')
    output = tackle('DerivedPython', a_str_required='bar')

    assert output['stuff'] == 'things'
    assert output['foo'] == 'bar'
    assert output['in_base'] == 'bar'
    assert output['a_str_required'] == 'bar'


def test_hooks_extends_required():
    """Check that we can extend a base that has required vars."""
    output = tackle('extends-required.yaml')

    assert output['call']['foo'] == 'bar'
    assert output['call']['bar'] == 'bar'
    assert output['call']['baz'] == 'bar'
    assert output['error_no_foo'] == 1
    assert output['error_no_bar'] == 1
    assert output['error_no_baz'] == 1
