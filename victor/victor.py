import logging
from functools import wraps

from .presenter import Presenter


def _configure_logging():
    logger = logging.getLogger('victor')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s %(name)s [%(levelname)s] %(message)s'))
    logger.addHandler(handler)


class Victor(object):
    def __init__(self):
        self.logger = logging.getLogger('victor')
        self.presenter = Presenter()
        self.enabled = True

    def debug(self, f, tick):
        if not self.enabled:
            return f

        @wraps(f)
        def wrapped(*args, **kwargs):
            start = tick()
            self.logger.debug(self.presenter.view_input(f, *args, **kwargs))

            result = f(*args, **kwargs)

            elasped_ms = (tick() - start) * 1000
            self.logger.debug(self.presenter.view_output(f, result, elasped_ms))

            return result

        return wrapped


# Only do this once
_configure_logging()

victor = Victor()
