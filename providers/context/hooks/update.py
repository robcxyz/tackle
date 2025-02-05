from typing import Any, Optional, Union

from tackle import BaseHook, Context, Field
from tackle.utils.data_crud import (
    encode_key_path,
    get_target_and_key,
    nested_get,
    nested_set,
)


class DictUpdateHook(BaseHook):
    """
    Hook for updating dict objects with values, appending list values, or overwriting
     string / int / float values.
    """

    hook_name = 'update'

    # fmt: off
    src: Union[dict, str, list] = Field(
        description="A dict to update and output the result or a str with separators "
                    "or list for a key path to the item update within the context.")
    input: Any = Field(description="The value to update the input `src`.")
    sep: str = Field('.', description="For string src's, a separator for key path.")
    # fmt: on

    args: list = ['src', 'input']

    def exec(self, context: Context) -> Optional[dict]:
        if isinstance(self.src, (str, list)):
            self.src = encode_key_path(self.src, self.sep)
        if isinstance(self.src, list):
            target_context, set_key_path = get_target_and_key(
                context, key_path=self.src
            )

            src = nested_get(
                element=target_context,
                keys=set_key_path,
            )
            if isinstance(src, dict):
                src.update(self.input)
            elif isinstance(src, list):
                src.append(self.input)
            else:
                # This overwrites the input
                nested_set(
                    element=target_context,
                    keys=set_key_path,
                    value=self.input,
                )
        else:
            self.src.update(self.input)
            return self.src
