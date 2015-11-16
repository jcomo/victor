from unittest import TestCase
from mock import patch

from victor import victor, debug


class LoggerState(object):
    def __init__(self):
        self.messages = []

    def record(self, message):
        self.messages.append(message)


class InMemoryLogger(object):
    def __init__(self):
        self.state = LoggerState()

    def debug(self, message):
        self.state.record(message)


class Counter(object):
    def __init__(self, step=1):
        self.step = step
        self.count = 0

    def __call__(self):
        count = self.count
        self.count += self.step
        return count


class DebugTestCase(TestCase):
    def setUp(self):
        super(DebugTestCase, self).setUp()
        self.logger = InMemoryLogger()
        victor.logger = self.logger
        victor.enabled = True

    def test_it_returns_evaluation_of_wrapped_function(self):

        @debug
        def f():
            return 'value'

        self.assertEqual('value', f())

    def test_it_returns_without_debugging_when_not_enabled(self):
        victor.enabled = False

        @debug
        def f():
            return 'value'

        self.assertEqual('value', f())
        self.assertEqual([], self.logger.state.messages)

    def test_it_reports_input_with_function_name_and_parameters(self):

        @debug
        def f(a, b):
            return

        f('test', 1)

        input_log = self.logger.state.messages[0]
        self.assertEqual("-> f('test', 1)", input_log)

    def test_it_reports_input_with_keyword_args(self):

        @debug
        def f(a, b, default=None):
            return

        f('test', 1, default=True)

        input_log = self.logger.state.messages[0]
        self.assertEqual("-> f('test', 1, default=True)", input_log)

    @patch('victor.api.time')
    def test_it_reports_output_with_time_elapsed(self, time_mock):
        time_mock.side_effect = Counter(step=1)

        @debug
        def f():
            return

        f()

        output_log = self.logger.state.messages[-1]
        self.assertEqual("<- f [1000.00ms]", output_log)

    @patch('victor.api.time')
    def test_it_reports_output_with_function_result(self, time_mock):
        time_mock.side_effect = Counter(step=1)

        @debug
        def f():
            return 'value'

        f()

        output_log = self.logger.state.messages[-1]
        self.assertEqual("<- f [1000.00ms] => 'value'", output_log)
