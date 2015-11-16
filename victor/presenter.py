from itertools import starmap

import six


class Presenter(object):
    def view_input(self, f, *args, **kwargs):
        arg_list = ', '.join(map(repr, args))
        if kwargs:
            keyword_arg_list = ', '.join(starmap(self._view_keyword_arg, six.iteritems(kwargs)))
            arg_list = '%s, %s' % (arg_list, keyword_arg_list)

        return '-> %s(%s)' % (f.__name__, arg_list)

    @staticmethod
    def _view_keyword_arg(name, value):
        return '%s=%s' % (name, repr(value))

    def view_output(self, f, result, elapsed_ms):
        profile = '[%.2fms]' % elapsed_ms
        if result:
            profile = '%s => %s' % (profile, repr(result))

        return '<- %s %s' % (f.__name__, profile)
