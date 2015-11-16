from itertools import starmap


class Presenter(object):
    def view_input(self, f, *args, **kwargs):
        arg_list = ', '.join(map(repr, args))
        if kwargs:
            keyword_arg_list = ', '.join(starmap(self._view_keyword_arg, kwargs.iteritems()))
            arg_list = '{}, {}'.format(arg_list, keyword_arg_list)

        return '-> {}({})'.format(f.__name__, arg_list)

    @staticmethod
    def _view_keyword_arg(name, value):
        return '{}={}'.format(name, repr(value))

    def view_output(self, f, result, elapsed_ms):
        profile = '[{:.2f}ms]'.format(elapsed_ms)
        if result:
            profile = '{} => {}'.format(profile, repr(result))

        return '<- {} {}'.format(f.__name__, profile)
