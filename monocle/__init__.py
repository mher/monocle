import sys

import core
from core import _o, o, launch

VERSION = '0.2'

_stack_name = None
def init(stack_name):
    global _stack_name
    _stack_name = stack_name
