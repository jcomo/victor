import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Import here since eggs aren't loaded outside of this scope
        import tox
        import shlex

        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)

        errno = tox.cmdline(args=args)
        sys.exit(errno)


setup(
    name = 'victor',
    version = '0.1.1',
    description = "A simple tool for debugging and profiling applications",
    url = 'https://github.com/jcomo/victor',
    author = 'Jonathan Como',
    author_email = 'jonathan.como@gmail.com',
    packages = find_packages(exclude=['docs', 'tests', 'scripts']),
    install_requires = [
        'six>=1.10',
    ],
    tests_require = ['tox'],
    cmdclass = {
        'test': Tox,
    },
    classifiers = [
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'debug profile python test'
)
