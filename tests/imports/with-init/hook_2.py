from tackle.models import BaseHook


class Hook2(BaseHook):
    hook_name: str = 'hook_2'

    is_public: bool = True

    def exec(self):
        return True
