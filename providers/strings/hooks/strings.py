from typing import Union

from tackle import BaseHook, Field


class SplitHook(BaseHook):
    """Hook for splitting a string into as list based on a separator."""

    hook_name: str = 'split'

    input: str = Field(..., description="A string to split into a list")
    separator: str = Field("/", description="String separator")

    args: list = ['input', 'separator']
    _docs_order = 2

    def exec(self):
        return self.input.split(self.separator)


class JoinHook(BaseHook):
    """Join a list of strings with a separator."""

    hook_name: str = 'join'

    input: list[Union[str, int]] = Field(
        ..., description="A list of strings to join.", render_by_default=True
    )
    separator: str = Field('', description="String separator.")

    args: list = ['input', 'separator']
    _docs_order = 3

    def exec(self):
        return self.separator.join(self.input)
