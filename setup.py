# -*- encoding: utf8 -*-
import glob
import io
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()

from setuptools.command.test import test as TestCommand
import sys


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
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)

setup(
    name="crash-dbseeder",
    version="0.1.0",
    license="MIT",
    description="ETL Crash Data",
    long_description="",
    author="Steve Gourley",
    author_email="SGourley@utah.gov",
    url="https://github.com/agrc/crash",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(i))[0] for i in glob.glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ],
    keywords=[
        # eg: "keyword1", "keyword2", "keyword3",
    ],
    install_requires=[
        "python-dateutil==2.3"
    ],
    dependency_links=[
        "http://iweb.dl.sourceforge.net/project/ceodbc/2.0.1/ceODBC-2.0.1.tar.gz"
    ],
    extras_require={
        # eg: 'rst': ["docutils>=0.11"],
    },
    entry_points={
        "console_scripts": [
            "dbseeder = dbseeder.__main__:main"
        ]
    },
    cmdclass={
        'test': Tox
    },
    tests_require=[
        'tox',
        'nose==1.3.4',
        'coverage==3.7.1'
    ],
)
