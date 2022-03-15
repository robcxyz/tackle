"""Special variables to be used in rendering."""

import os
import platform

import csv

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tackle.models import Context


def get_linux_distribution():
    """Return the equivalent of lsb_release -a."""
    if platform.system() == 'Linux':
        RELEASE_DATA = {}
        with open("/etc/os-release") as f:
            reader = csv.reader(f, delimiter="=")
            for row in reader:
                if row:
                    RELEASE_DATA[row[0]] = row[1]
        if RELEASE_DATA["ID"] in ["debian", "raspbian"]:
            with open("/etc/debian_version") as f:
                DEBIAN_VERSION = f.readline().strip()
            major_version = DEBIAN_VERSION.split(".")[0]
            version_split = RELEASE_DATA["VERSION"].split(" ", maxsplit=1)
            if version_split[0] == major_version:
                # Just major version shown, replace it with the full version
                RELEASE_DATA["VERSION"] = " ".join([DEBIAN_VERSION] + version_split[1:])
        return "{} {}".format(RELEASE_DATA["NAME"], RELEASE_DATA["VERSION"])
    else:
        return None


def _cwd():
    return os.getcwd()


def _home_dir():
    return os.path.expanduser('~')


def _system():
    return platform.system()


def _platform():
    return platform.platform()


def _release():
    return platform.release()


def _version():
    return platform.version()


def _processor():
    return platform.processor()


def _architecture():
    return platform.architecture()


def _calling_directory(context: 'Context'):
    return context.calling_directory


def _calling_file(context: 'Context'):
    return context.calling_file


def _current_file(context: 'Context'):
    return context.input_file


def _current_directory(context: 'Context'):
    return context.input_dir


def _this(context: 'Context'):
    return dict(context.output_dict)


def _output(context: 'Context'):
    return context.output_dict


special_variables = {
    'cwd': _cwd,
    'home_dir': _home_dir,
    'system': _system,
    'platform': _platform,
    'version': _version,
    'processor': _processor,
    'architecture': _architecture,
    'lsb_release': get_linux_distribution,
    'calling_directory': _calling_directory,
    'calling_file': _calling_file,
    'current_file': _current_file,
    'current_directory': _current_directory,
    'this': _this,
    'output': _output,
}
