# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import os

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


class COLORS(object):
    BLACK = BLACK
    RED = RED
    GREEN = GREEN
    YELLOW = YELLOW
    BLUE = BLUE
    MAGENTA = MAGENTA
    CYAN = CYAN
    WHITE = WHITE


RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


def colored_string(msg, color):
    return COLOR_SEQ % (30 + color) + msg + RESET_SEQ


def print_console(msg, color=None):
    if color:
        msg = colored_string(msg, color)
    sys.stdout.write(msg + os.linesep)


def import_string(module_name):
    try:
        __import__(module_name)
    except ImportError:
        if '.' not in module_name:
            raise
    else:
        return sys.modules[module_name]

    module_name, obj_name = module_name.rsplit('.', 1)
    try:
        module = __import__(module_name, None, None, [obj_name])
    except ImportError:
        module = import_string(module_name)
    try:
        return getattr(module, obj_name)
    except AttributeError as e:
        raise ImportError(e)


def get_files(dir_path, recursive=False, extension=None):
    files = []
    ext = None
    if extension:
        ext = ".%s" % extension
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if ext and not f.endswith(ext):
                continue
            yield os.path.join(root, f)
        if recursive:
            for d in dirs:
                for f in get_files(d, recursive, extension):
                    yield os.path.join(root, f)
