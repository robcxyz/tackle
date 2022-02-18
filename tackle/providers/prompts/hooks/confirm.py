import sys
from PyInquirer import prompt
from typing import Any

from tackle.models import BaseHook, Field
from tackle.utils.dicts import get_readable_key_path


class InquirerConfirmHook(BaseHook):
    """
    Hook to confirm with a message and return a boolean.
     [Source example](https://github.com/CITGuru/PyInquirer/blob/master/examples/confirm.py)
    """

    hook_type: str = 'confirm'

    default: bool = Field(True, description="Default choice.")
    message: str = Field(None, description="String message to show when prompting.")

    _args: list = ['message']
    _docs_order = 4

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.message is None:
            self.message = get_readable_key_path(self.key_path) + ' >>>'

    def execute(self) -> bool:
        if not self.no_input:
            question = {
                'type': 'confirm',
                'name': 'tmp',
                'message': self.message,
                'default': self.default,
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
            # When no_input then return empty list
            return True
