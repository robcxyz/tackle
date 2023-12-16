import sys
from InquirerPy import prompt

from typing import Any

from tackle import BaseHook, Field, Context
from tackle.utils.data_crud import get_readable_key_path
from tackle import exceptions


class InquirerEditorHook(BaseHook):
    """
    Hook for PyInquirer `editor` type prompts. Opens an editor like nano to fill in a
     field. [Source example](https://github.com/kazhala/InquirerPy/blob/master/examples/editor.py)
    """

    hook_name: str = 'editor'
    default: Any = Field(None, description="Default selection.")
    message: str = Field(None, description="String message to show when prompting.")

    args: list = ['message', 'default']

    def exec(self, context: Context) -> bool:
        if self.message is None:
            self.message = get_readable_key_path(context.key_path) + ' >>>'

        if not context.no_input:
            question = {
                'type': self.hook_name,
                'name': 'tmp',
                'message': self.message,
                'default': self.default,
            }

            # Handle keyboard exit
            try:
                response = prompt([question])
            except KeyboardInterrupt:
                print("Exiting...")
                sys.exit(0)
            except EOFError:
                raise exceptions.PromptHookCallException(context=context)
            return response['tmp']

        elif self.default:
            return self.default
        else:
            # When no_input then return empty list
            return True
