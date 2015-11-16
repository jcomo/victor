from time import time

from .victor import victor


def debug(f):
    return victor.debug(f, time)
