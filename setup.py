# -*- coding: utf-8 -*-
import os
<<<<<<< HEAD
import re


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


long_description = read("README.rst")


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")
=======
import subprocess
import sys
from shutil import rmtree
from setuptools import setup, find_packages, Command
import codecs

__version__ = None
exec(open("slack/version.py").read())

here = os.path.abspath(os.path.dirname(__file__))

long_description = ""
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()

tests_require = ["pytest", "pytest-cov", "codecov", "flake8", "black"]


class BaseCommand(Command):
    """Base Command"""

    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def _run(self, s, command):
        try:
            self.status(s + "\n" + " ".join(command))
            subprocess.check_call(command)
        except subprocess.CalledProcessError as error:
            sys.exit(error.returncode)


class UploadCommand(BaseCommand):
    """Support setup.py upload. Thanks @kennethreitz!"""

    description = "Build and publish the package."

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self._run(
            "Building Source and Wheel (universal) distribution…",
            [sys.executable, "setup.py", "sdist", "bdist_wheel", "--universal"],
        )

        self._run(
            "Installing Twine dependency…",
            [sys.executable, "-m", "pip", "install", "twine"],
        )

        self._run(
            "Uploading the package to PyPI via Twine…",
            [sys.executable, "-m", "twine", "upload", "dist/*"],
        )

        self._run("Creating git tags…", ["git", "tag", f"v{__version__}"])
        self._run("Pushing git tags…", ["git", "push", "--tags"])


class ValidateCommand(BaseCommand):
    """Support setup.py validate."""

    description = "Run Python static code analyzer (flake8), formatter (black) and unit tests (pytest)."

    def run(self):
        self._run(
            "Installing test dependencies…",
            [sys.executable, "-m", "pip", "install"] + tests_require,
        )
        self._run("Running black…", [sys.executable, "-m", "black", f"{here}/slack"])
        self._run("Running flake8…", [sys.executable, "-m", "flake8", f"{here}/slack"])
        self._run(
            "Running pytest…",
            [
                sys.executable,
                "-m",
                "pytest",
                "--cov-report=xml",
                f"--cov={here}/slack",
                "tests/",
            ],
        )
>>>>>>> 415389d64f38ab19e776b94514d5c9f6eae1fdcc


setup(
    name="slackclient",
<<<<<<< HEAD
    version=find_version("slack", "version.py"),
=======
    version=__version__,
>>>>>>> 415389d64f38ab19e776b94514d5c9f6eae1fdcc
    description="Slack API clients for Web API and RTM API",
    long_description=long_description,
    url="https://github.com/slackapi/python-slackclient",
    author="Slack Technologies, Inc.",
    author_email="opensource@slack.com",
<<<<<<< HEAD
=======
    python_requires=">=3.6.0",
    include_package_data=True,
>>>>>>> 415389d64f38ab19e776b94514d5c9f6eae1fdcc
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Communications :: Chat",
        "Topic :: System :: Networking",
        "Topic :: Office/Business",
        "License :: OSI Approved :: MIT License",
<<<<<<< HEAD
=======
        "Programming Language :: Python",
>>>>>>> 415389d64f38ab19e776b94514d5c9f6eae1fdcc
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="slack slack-web slack-rtm chat chatbots bots chatops",
<<<<<<< HEAD
    packages=find_packages(exclude=["docs", "docs-src", "tests"]),
    install_requires=["websockets<7.0", "requests<2.21"],
=======
    packages=find_packages(exclude=["docs", "docs-src", "tests", "tests.*"]),
    install_requires=["websockets>6.0", "requests>2.20"],
    setup_requires=["pytest-runner"],
    test_suite="tests",
    tests_require=tests_require,
    cmdclass={"upload": UploadCommand, "validate": ValidateCommand},
>>>>>>> 415389d64f38ab19e776b94514d5c9f6eae1fdcc
)
