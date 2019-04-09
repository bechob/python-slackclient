# Python slackclient
The Python slackclient is adeveloper kit for interfacing with the Slack Web API and Real Time Messaging (RTM) API on Python 3.6 and above.



[![pypi package][pypi-image]][pypi-url]
[![Build Status][travis-image]][travis-url]
[![Build Status][windows-build-status]][windows-build-url]
[![Python Version][python-version]][pypi-url]
[![codecov][codecov-image]][codecov-url]
[![contact][contact-image]][contact-url]


Whether you're building a custom app for your team, or integrating a third party service into your Slack workflows, Slack Developer Kit for Python allows you to leverage the flexibility of Python to get your project up and running as quickly as possible.

The **Python slackclient** allows interaction with:

- The Slack web api methods available at our [Api Docs site][api-methods]
- Interaction with our [RTM API][rtm-docs]

If you want to use our [Events API][events-docs], please check the [Slack Events API adapter for Python][python-slack-events-api]

![](header.png)

## Table of contents
* [Requirements](#requirements)
* [Installation](#installation)
* [Build your first app](#begin)

## Requirements

This Library requires Python 3.6 and above. If you require Python 2, please use our SlackClient v1.3.1. If you're unsure how to check what version of Python you're on, you can check it using the following:

```bash
python --version
```
We will be using [PipEnv][pipenv] for our examples but if you wish to use pip or similar, you can.

> Note: You may need to use `python3` before your commands to ensure you 


## Installation

We recommend using [PyPI][pypi] to install Slack Developer Kit for Python as well as [PipEnv][pipenv]


```bash
pipenv install --python 3.6 slackclient
```

If you require Python 2 support, you can use the following to install the previous version of our Developer Kit

```bash
pipenv install --python 2.6 slackclient==1.3.1
```


## Begin

Link to the "Build an app in 10 minutes" guide

_For more examples and usage, please refer to the [Slack API Documentation site][api-docs]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

<details>
  <summary><strong>Release History</strong> (click to expand)</summary>

<!-- rel -->

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
* 0.0.1
    * Work in progress
<!-- relstop -->


</details>

## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[pypi-image]: https://badge.fury.io/py/slackclient.svg
[pypi-url]: https://pypi.python.org/pypi/slackclient
[windows-build-status]: https://ci.appveyor.com/api/projects/status/rif04t60ptslj32x/branch/master?svg=true
[windows-build-url]: https://ci.appveyor.com/project/slackapi/python-slackclient
[travis-image]: https://travis-ci.org/slackapi/python-slackclient.svg?branch=master
[travis-url]: https://travis-ci.org/slackapi/python-slackclient
[python-version]:  https://img.shields.io/pypi/pyversions/slackclient.svg
[codecov-image]: https://codecov.io/gh/slackapi/python-slackclient/branch/master/graph/badge.svg
[codecov-url]: https://codecov.io/gh/slackapi/python-slackclient
[contact-image]: https://img.shields.io/badge/contact-support-green.svg
[contact-url]: https://slack.com/support
[api-docs]: https://api.slack.com
[slackclientv1]: https://github.com/slackapi/python-slackclient/
[api-methods]: https://api.slack.com/methods
[rtm-docs]: https://api.slack.com/rtm
[events-docs]: https://api.slack.com/events-apiq
[python-slack-events-api]: https://github.com/slackapi/python-slack-events-api
[pypi]: https://pypi.python.org/pypi
[pipenv]: https://pypi.org/project/pipenv/