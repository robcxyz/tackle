import sys
from PyInquirer import prompt
from typing import Any

from tackle.models import BaseHook, Field
from tackle.utils.dicts import get_readable_key_path


class InquirerPasswordHook(BaseHook):
    """
    Hook for PyInquirer `password` type prompts. Masks the input as the user types it
     in. [Source example](https://github.com/CITGuru/PyInquirer/blob/master/examples/password.py)
    """

    hook_type: str = 'password'

    default: Any = Field(None, description="Default choice.")
    message: str = Field(None, description="String message to show when prompting.")

    _args: list = ['message', 'default']

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.message is None:
            self.message = get_readable_key_path(self.key_path) + ' >>>'

    def execute(self) -> str:
        if not self.no_input:
            question = {
                'type': self.hook_type,
                'name': 'tmp',
                'message': self.message,
                # 'default': self.default,
            }

            response = prompt([question])

            # Handle keyboard exit
            try:
                return response['tmp']
            except KeyError:
                sys.exit(0)
        elif self.default:
            return self.default
        else:
            return ""
