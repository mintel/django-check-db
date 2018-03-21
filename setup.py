#!/usr/bin/env python
import contextlib
import io
import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

# Dependencies for this Python library.
REQUIRES = [
    'django',
]

# Dependencies to run the tests for this Python library.
TEST_REQUIREMENTS = [
    'pytest',
]

HERE = os.path.dirname(os.path.abspath(__file__))


def setup_package():
    with chdir(HERE):
        with io.open(os.path.join('django_check_db', '_version.py'), 'r', encoding='utf8') as f:
            about = {}
            exec(f.read(), about)

        with io.open('README.rst', 'r', encoding='utf8') as f:
            readme = f.read()
    setup(
        name=about['__title__'],
        version=about['__version__'],
        description=about['__summary__'],
        long_description=readme,
        author=about['__author__'],
        author_email=about['__author_email__'],
        license='MIT',
        url=about['__uri__'],
        packages=['django_check_db'],
        install_requires=REQUIRES,
        tests_require=TEST_REQUIREMENTS,
        extras_require={'test': TEST_REQUIREMENTS},
        cmdclass={'test': PyTest},
        zip_safe=True,
        classifiers=(
            'Development Status :: 4 - Beta',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python',
            'Topic :: Database',
            'Topic :: Software Development :: Libraries',
            'Topic :: Utilities',
        ),
    )


@contextlib.contextmanager
def chdir(new_dir):
    old_dir = os.getcwd()
    try:
        os.chdir(new_dir)
        sys.path.insert(0, new_dir)
        yield
    finally:
        del sys.path[0]
        os.chdir(old_dir)


class PyTest(TestCommand):
    """Setup the py.test test runner."""

    def finalize_options(self):
        """Set options for the command line."""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """Execute the test runner command."""
        import pytest
        sys.exit(pytest.main(self.test_args))


if __name__ == "__main__":
    setup_package()
