# *nbapy - [stats.nba.com](https://stats.nba.com) API for python*

## Summary
A python facing API for `stats.nba.com`

***Warning*** `stats.nba.com` is notorious for being extremely unreliable. Please report any issues you find.

## Documentation / Usage
An ongoing process, but check out the [wiki](https://github.com/jtpavlock/nbapy/wiki), the [jupyter notebook docs](https://github.com/jtpavlock/nbapy/tree/master/docs/), or feel free to poke around the codebase.

## Installation
To install from pypi:

```
$ pip install nbapy
```

Else:
- Download from source (git clone, zipped package)
- Run from the root directory:

```
$ pip install .
```

## Contributing
#### 1. Fork the repository and create a feature/bug fix branch

#### 2. Install development requirements
`$ pip install -e . ".[dev]"`

#### 3. Hack away

*Coding conventions*

* [black](https://github.com/psf/black) for formatting
* [google docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
* [flake8](https://flake8.pycqa.org/en/latest/index.html#quickstart) for linting
* [mypy](http://mypy-lang.org/) for static typing analysis

*Optional (but recommended)*

`nbapy` has a [pre-commit](https://pre-commit.com/) file that you can install to automatically enforce these conventions prior to committing via a git hook.

To install: `$ pre-commit install`

You can also use `$ pre-commit run -a` to run the checks manually.

#### 4. Create some tests

#### 5. Make sure everything looks good
`$ pytest --cov`* 

`$ pre-commit run -a` (if you didn't install the pre-commit git hook)

\* note the first time you run this, it may take a few minutes. However, the requests will cache, and subsequent runs should be much faster.

#### 6. Submit a pull request

Other ways to contribute involve submitting any issues or adding some documentation!

## To-Do
- Finish Jupyter Notebook documentation
