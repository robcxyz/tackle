import sys
from InquirerPy import prompt

from typing import Any
from tackle import BaseHook, Field, Context
from tackle.utils.data_crud import get_readable_key_path
from tackle import exceptions


class InquirerExpandHook(BaseHook):
    """
    Hook for PyInquirer `expand` type prompt.
     [Source example](https://github.com/kazhala/InquirerPy/blob/master/examples/expand.py)
    """

    hook_name: str = 'expand'

    default: Any = Field(None, description="Default selection.")
    message: str = Field(None, description="String message to show when prompting.")

    args: list = ['message', 'default']

    def exec(self, context: Context) -> list:
        if self.message is None:
            self.message = get_readable_key_path(context.key_path) + ' >>>'

        if not context.no_input:
            question = {
                'type': self.hook_name,
                'name': 'tmp',
                'message': self.message,
            }
            if self.default:
                question.update({'default': self.default})

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
            return []
