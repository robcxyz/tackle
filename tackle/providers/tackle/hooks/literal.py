from typing import Any

from tackle.models import BaseHook, Field


class LiteralHook(BaseHook):
    """Literally return the input."""

    hook_type: str = 'literal'
    input: Any = Field(..., description="Any variable input.")

    _args: list = ['input']

    def execute(self) -> Any:
        return self.input
