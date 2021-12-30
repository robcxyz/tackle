"""Select hook."""
import os
import json
import logging
import requests
from typing import Optional, Dict, List, Union

from tackle.models import BaseHook

logger = logging.getLogger(__name__)


def exit_none_200(r: requests.Response, no_exit: bool, url: str):
    """Exit if the status code is not 2xx."""
    if not (r.status_code - 200) < 100 and not no_exit:
        raise requests.exceptions.HTTPError(
            f"Error sending request to {url}, got '{r.status_code}' status code."
        )


def process_content(r: requests.Response):
    """Output the content based on the header."""
    if 'application/json' in r.headers['Content-Type']:
        return json.loads(r.content)
    elif 'text/plain' in r.headers['Content-Type']:
        return r.content


class RequestsGetHook(BaseHook):
    """
    Hook for Requests 'get' type prompts.

    :param message: String message to show when prompting.
    :return: Response of request in a dict
    """

    hook_type: str = 'get'
    no_exit: bool = False

    url: str = None
    kwargs: dict = {}
    params: dict = None
    # Requests API docs call for additional functionality not for yaml
    # params: Union[Dict, List[tuple], bytes] = None

    _args: list = [
        'url',
        'kwargs',
        'params',
    ]

    def execute(self) -> dict:
        r = requests.get(self.url, params=self.params, **self.kwargs)
        exit_none_200(r, self.no_exit, self.url)
        return process_content(r)


class RequestsPostHook(BaseHook):
    """
    Hook for Requests 'post' type prompts.

    :param message: String message to show when prompting.
    :return: Response of request in a dict
    """

    hook_type: str = 'post'
    no_exit: bool = False

    url: str
    kwargs: dict = {}

    # Requests API docs call for additional functionality not for yaml
    data: Union[dict, list, str] = None
    # data: Optional[Union[Dict, List[tuple], bytes, str]]
    input_json: dict = None

    _args: list = ['url', 'data', 'kwargs']

    def execute(self) -> dict:
        if isinstance(self.data, str):
            if not os.path.exists(self.data):
                raise FileNotFoundError(
                    f"For the requests patch method, data fields must be a "
                    f"reference to a file path, not {self.data}."
                )

        r = requests.post(self.url, data=self.data, json=self.input_json, **self.kwargs)
        exit_none_200(r, self.no_exit, self.url)

        return r.json()


class RequestsPutHook(BaseHook):
    """
    Hook for Requests 'put' type prompts.

    :param message: String message to show when prompting.
    :return: Response of request in a dict
    """

    hook_type: str = 'put'
    no_exit: bool = False

    url: str
    kwargs: Dict = {}
    data: Optional[Union[Dict, List[tuple], bytes, str]]
    input_json: Optional[dict] = None

    _args: list = ['url', 'data', 'kwargs']

    def execute(self):
        if isinstance(self.data, str):
            if not os.path.exists(self.data):
                raise FileNotFoundError(
                    f"For the requests patch method, data fields must be a "
                    f"reference to a file path, not {self.data}."
                )

        r = requests.put(self.url, data=self.data, json=self.input_json, **self.kwargs)
        exit_none_200(r, self.no_exit, self.url)

        return r.json()


class RequestsPatchHook(BaseHook):
    """
    Hook for Requests 'patch' type prompts.

    :param message: String message to show when prompting.
    :return: Response of request in a dict
    """

    hook_type: str = 'patch'
    no_exit: bool = False

    url: str
    kwargs: Dict = {}
    data: Optional[Union[Dict, List[tuple], bytes, str]]
    input_json: Optional[dict] = None

    _args: list = ['url', 'data', 'kwargs']

    def execute(self):
        if isinstance(self.data, str):
            if not os.path.exists(self.data):
                raise FileNotFoundError(
                    f"For the requests patch method, data fields must be a "
                    f"reference to a file path, not {self.data}."
                )

        r = requests.patch(
            self.url, data=self.data, json=self.input_json, **self.kwargs
        )
        exit_none_200(r, self.no_exit, self.url)

        return r.json()


class RequestsDeleteHook(BaseHook):
    """
    Hook for Requests 'delete' type prompts.

    Wraps https://docs.python-requests.org/en/latest/api/
    """

    hook_type: str = 'delete'
    url: str
    kwargs: Dict = {}
    no_exit: bool = False

    _args: list = ['url', 'kwargs', 'params']

    def execute(self):
        r = requests.delete(self.url, **self.kwargs)
        exit_none_200(r, self.no_exit, self.url)

        return r.status_code
