"""
Declarative hook macros. Handles all the inputs to hooks (ie `hook_name<-`). Removes
any arrows from keys based on if they are hook calls or methods.
"""
from typing import TYPE_CHECKING

from tackle import exceptions

from tackle.models import DclHookInput

if TYPE_CHECKING:
    from tackle.models import Context

FUNCTION_ARGS = {
    DclHookInput.model_fields[i].alias
    if DclHookInput.model_fields[i].alias is not None else
    i for i in DclHookInput.model_fields.keys()
}


def dict_hook_method_macros():
    pass


from tackle.methods import new_default_methods

DEFAULT_METHODS = new_default_methods()


def update_value_with_default_factory(context: Context, hook_name: str, value: dict):
    """
    Create a default factory walker and update the value with the new key.
    """
    from tackle.parser import create_dict_default_factory_executor

    default_factory = value.pop(key)
    value['default_factory'] = {
        'return->': create_dict_default_factory_executor(
            context=context,
            value=default_factory,
        )
    }




DEFAULT_FACTORY_KEYS = [
    'default->',
    'default_>',
    'default_factory->',
    'default_factory_>',
    '->',
    '_>',
]


def update_default_factory_hook_fields(
        context: Context,
        hook_name: str,
        value: dict,
):
    """
    Any `default` or `default_factory` key ending in an arrow will be transformed into
     a `default_factory` field with the arrow indicating if the field is excluded or
     included based on the access modifier (-> vs _>) of the arrow. Reasoning is arrows
     indicate parsables so an arrow ending in an arrow must be a default_factory field
     which is callable so this function is sort pre-process before that callable is
     assembled.

    Examples:
     public / included `->` or private / excluded `_>`.
     default_>: {...} => default_factory: {excluded: True, ...}
    """
    for i in DEFAULT_FACTORY_KEYS:
        if i in value:
            raw_field = value.pop(i)
            if 'default_factory' in value:
                raise exceptions.MalformedHookFieldException(
                    f"Cannot have both '{i}' and 'default_factory' in hook field.",
                    context=context, hook_name=hook_name,
                )
            value['default_factory'] = raw_field
            if i[-2:] == '_>':
                value['exclude'] = True
            break


def expand_default_factory(
        value: dict,
        key: str,
):
    """
    Expand keys for special cases where we have string values or bare arrows as a key
     which both indicate hook calls. Ignores anything that doesn't have a
     `default_factory` field which this acts on.
    """
    if 'default_factory' not in value:
        pass
    elif isinstance(value['default_factory'], str):
        # Convert to dict which then returns the key
        value['default_factory'] = {
            f'{key}->': value['default_factory'],
            'return->': "{{" + key + "}}",
        }
    elif '->' in value['default_factory'] or '_>' in value['default_factory']:
        # Already have whole arrow so nest value in a key and return that
        value['default_factory'] = {
            key: value['default_factory'],
            'return->': "{{" + key + "}}",
        }


def infer_type_from_default(value: dict):
    """When a `default` field exists but not a `type` we infer the type."""
    if 'default' in value and 'type' not in value:
        # Has default field but not a type so assuming the type is the default.
        default = value['default']
        if isinstance(default, ScalarFloat):
            value['type'] = 'float'
        elif isinstance(default, CommentedSeq):
            value['type'] = 'list'
        elif isinstance(default, CommentedMap):
            value['type'] = 'dict'
        else:
            value['type'] = type(value['default']).__name__
        return value
    elif 'default_factory' in value and 'type' not in value:
        value['type'] = 'Any'


# Any of these fields and the value is a field
MINIMAL_FIELD_KEYS = [
    'type',
    'default',
    'default_factory',
    'enum',
]

def is_field(value: dict) -> bool:
    """
    Determines if a value is a pydantic field or if it is just a dict. Some minimal
     fields are required for it to be a field.
    """
    for i in MINIMAL_FIELD_KEYS:
        if i in value:
            return True
    return False


def create_default_factory(
        context: Context,
        hook_name: str,
        value: dict,
        value_is_factory: bool = False,
):
    """
    Create a default_factory field out of the value which is a callable that parses the
     data calling hooks if they exist.
    """
    from tackle.parser import create_dict_default_factory_executor

    if value_is_factory:
        default_factory = value
    else:
        default_factory = value.pop('default_factory')

    if isinstance(default_factory, (dict, list)):
        default_factory_value = default_factory
    else:
        raise exceptions.MalformedHookFieldException(
            "The default_factory must be a string (compact hook call), "
            "dict, or list which will be parsed.",
            context=context, hook_name=hook_name,
        )

    value['default_factory'] = create_dict_default_factory_executor(
        context=context,
        value=default_factory_value,
    )



def dict_field_hook_macro(
        context: Context,
        hook_name: str,
        key: str,
        value: dict,
) -> dict:
    """
    Transform dict values so that they are parseable by creating a callable as a
     default factory that includes the dict. This will be called unless a value is
     given. Handles cases when a type is not given which it then assumes as `Any` since
     it is not known. Handles a lot of edge cases such as:

     field->: a_hook args
     field: {->: a_hook, key: value}
     field: {default->: a_hook args}
     field: {random_key: {->: a_hook args}}

    In all these cases it makes a callable parseable dict as a default_factory.
    """
    # Transform fields ending in a hook call to a field with a default factory
    update_default_factory_hook_fields(context, hook_name=hook_name, value=value)

    # Expand any default_factory fields - value = str or dict with arrow
    expand_default_factory(value=value, key=key)

    # When a `default` field exists but not a `type` field we infer the `type`
    infer_type_from_default(value=value)

    # Check minimal fields to see if we can just return the value as a default factory
    if not is_field(value):
        # Just make dict values parseable
        create_default_factory(
            context=context,
            hook_name=hook_name,
            value=value,
            value_is_factory=True,
        )
        value['type'] = 'Any'
        return value



def str_field_hook_macro(
        context: Context,
        hook_name: str,
        key: str,
        value: dict,
) -> dict:
    if not isinstance(value, str):
        raise exceptions.MalformedHookFieldException(
            f"The field hook at key={key[-2:]} must have a string value.",
            context=context, hook_name=hook_name,
        )
    return dict_field_hook_macro(
        context=context,
        hook_name=hook_name,
        key=key[:-2],
        value={f'default_factory{key[-2:]}': value},
    )


# DCL_HOOK_FIELDS = [
#     k if v.alias is None else v.alias for k, v in DclHookInput.model_fields.items()
# ]

def hook_dict_macro(
        context: 'Context',
        hook_input_raw: dict,
        hook_name: str,
) -> dict:
    """Remove any arrows from keys."""
    new_hook_input = {}
    # Special case where we don't need an arrow
    if 'exec' in hook_input_raw:
        new_hook_input['exec<-'] = hook_input_raw.pop('exec')

    for k, v in hook_input_raw.items():
        if k.endswith(('<-', '<_')):
            # We have a method. Value handled elsewhere
            new_hook_input[k[-2:]] = {k[-2:]: v}
        elif k.endswith(('->', '_>')):
            if not isinstance(v, str):
                raise exceptions.UnknownInputArgumentException(
                    f"Hook definition fields ending with arrow (ie `{k}`) must have"
                    f" string values.", context=context
                )
            arrow = k[-2:]
            # exclude = True if arrow == '_>' else False
            new_hook_input[k[:-2]] = {
                'default': v,
                'exclude': True if arrow == '_>' else False,
                'parse_keys': ['default']
            }
        elif v is None:
            new_hook_input[k] = {'type': 'Any', 'default': None}
        elif isinstance(v, str) and v in LITERAL_TYPES:
            new_hook_input[k] = {'type': v}
        elif isinstance(v, dict):
            # dict inputs need to be checked for keys with an arrow (ie default->)
            # TODO: Traverse and apply logic

            new_hook_input[k] = v
        else:
            # Otherwise just put as default value with same type
            new_hook_input[k] = {'type': type(v).__name__, 'default': v}

    return new_hook_input


def str_hook_macro(hook_input_raw: str) -> dict:
    """
    String hook macro converts to a dict that executes and returns the key as a hook.
    From: foo<-: literal bar
    To: foo<-:
          tmp_in->: literal bar
          tmp_out->: return {{tmp_in}}
    """
    return {'tmp_in->': hook_input_raw, 'tmp_out->': 'return {{tmp_in}}'}


def hook_macros(context: 'Context', hook_input_raw: dict | str) -> dict:
    """
    Macro to update the keys of a declarative hook definition and parse out any methods.
    """

    if isinstance(hook_input_raw, str):
        return str_hook_macro(hook_input_raw=hook_input_raw)
    elif isinstance(hook_input_raw, dict):
        return dict_hook_macro(context=context, hook_input_raw=hook_input_raw)
    else:
        raise Exception("This should never happen...")
