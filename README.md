<p align="center">
<a href="https://github.com/jtpavlock/nbapy/actions"><img alt="Actions Status" src="https://github.com/jtpavlock/nbapy/workflows/CI/badge.svg"></a>
<a href="https://pypi.org/project/nbapy/"><img alt="PyPI" src="https://img.shields.io/pypi/v/nbapy"></a>
<a href="https://pepy.tech/project/nbapy"><img alt="Downloads" src="https://pepy.tech/badge/nbapy"></a>
</p>

# *nbapy - [stats.nba.com](https://stats.nba.com) API for python*

## Summary
A python facing API for `stats.nba.com`

***Warning*** `stats.nba.com` is notorious for being extremely unreliable. Please report any issues you find.

## Usage

All data is returned as a pandas dataframe (check out the [starter docs](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html) if you're new to pandas). For example:

```python
from nbapy import game
import pandas as pd

game_id = '0021900017'  # taken from 'https://stats.nba.com/game/0021900017/'
stats = game.BoxScore(game_id).players_stats()
print(stats)
```

If you want to cache results so you don't have to reach the api every time, you can use [requests-cache](https://pypi.org/project/requests-cache/)
```python
from nbapy import game
import pandas as pd
import requests_cache

requests_cache.install_cache('nbapy_cache')

game_id = '0021900017'
stats = game.BoxScore(game_id).players_stats()
print(stats)
```

## Documentation
Not currently exhaustive (PRs are welcome!), but check out [the jupyter notebook examples](https://github.com/jtpavlock/nbapy/tree/master/docs/examples), or feel free to poke around the codebase.


## Installation
To install from pypi:

```bash
$ python -m pip install nbapy
```

## Contributing
#### 1. Fork the repository and create a feature/bug fix branch

#### 2. Install development requirements

You will to first install [poetry](https://pypi.org/project/poetry/) if you don't already have it.
```bash
$ python -m pip install poetry
```

After that, just run `poetry install` inside of your fork.

#### 3. Hack away

*Coding conventions*

* [black](https://github.com/psf/black) for formatting
* [google docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
* [flake8](https://flake8.pycqa.org/en/latest/index.html#quickstart) for linting
* [mypy](http://mypy-lang.org/) for static typing analysis
* [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit style.
* [isort](https://github.com/timothycrosley/isort/) for import organization.

Whew, that's a lot, but I'm a big fan of clean code, and I hope you are too! The good news is that if you follow the following advice, you'll find these aren't too hard to manage :smile:

*Optional (but recommended)*

`nbapy` has a [pre-commit](https://pre-commit.com/) file that you can install to automatically enforce these conventions prior to committing via a git hook.

To install: `$ pre-commit install`

You can also use `$ pre-commit run -a` to run the checks manually.

For commit messages, I recommend using [commitizen](https://github.com/commitizen-tools/commitizen). It is automatically installed in the dev dependencies, so to commit, you just run `cz c` and follow the prompts.

If you're using pre-commit, and either the black or isort check fails, the good news is it will fix the problems for you. However, it won't continue the commit automatically so that you get a chance to look over the changes. You'll have to re-stage the changes, and then you can run `cz c --retry` so you don't lose that nice commit message you just wrote.

#### 4. Create some tests

#### 5. Make sure everything looks good
`$ pytest --cov`* 

`$ sphinx-build -W -q -b html docs docs/_build/html`

`$ pre-commit run -a` (if you didn't install the pre-commit git hook)

\* note the first time you run this, it may take a few minutes. However, the requests will cache, and subsequent runs should be much faster.

#### 6. Submit a pull request

Other ways to contribute involve submitting any issues or adding some documentation!

## To-Do
- Finish Jupyter Notebook documentation

## Authors

This is orginally based off of https://github.com/seemethere/nba_py so a lot of the work was done by those guys. My goal with this project is to clean up the code, add some proper documentation, and keep it up to date.
