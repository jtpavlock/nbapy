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
stats = pd.DataFrame(game.BoxScore(game_id).players_stats())
```

If you want to cache results so you don't have to reach the api every time, you can use [requests-cache](https://pypi.org/project/requests-cache/)
```python
from nbapy import game
import pandas as pd
import requests_cache

requests_cache.install_cache('nbapy_cache')

game_id = '0021900017'
stats = pd.DataFrame(game.BoxScore(game_id).players_stats())
```

## Documentation
Not currently exhaustive (PRs are welcome!), but check out [the jupyter notebook docs](https://github.com/jtpavlock/nbapy/tree/master/docs), or feel free to poke around the codebase.


## Installation
To install from pypi:

```bash
$ python -m pip install nbapy
```

Else:
- Download from source (git clone, zipped package)
- Run from the root directory:

```bash
$ python -m pip install .
```

## Contributing
#### 1. Fork the repository and create a feature/bug fix branch

#### 2. Install development requirements
```bash
$ python -m pip install -e . ".[dev]"
```

#### 3. Hack away

*Coding conventions*

* [black](https://github.com/psf/black) for formatting
* [google docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
* [flake8](https://flake8.pycqa.org/en/latest/index.html#quickstart) for linting
* [mypy](http://mypy-lang.org/) for static typing analysis
* [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit style.

*Optional (but recommended)*

`nbapy` has a [pre-commit](https://pre-commit.com/) file that you can install to automatically enforce these conventions prior to committing via a git hook.

To install: `$ pre-commit install`

You can also use `$ pre-commit run -a` to run the checks manually.

For commit messages, I recommend using [commtizen](https://github.com/commitizen-tools/commitizen). It is automatically installed in the dev dependencies, so to commit, you just run `cz c` and follow the prompts.

#### 4. Create some tests

#### 5. Make sure everything looks good
`$ pytest --cov`* 

`$ pre-commit run -a` (if you didn't install the pre-commit git hook)

\* note the first time you run this, it may take a few minutes. However, the requests will cache, and subsequent runs should be much faster.

#### 6. Submit a pull request

Other ways to contribute involve submitting any issues or adding some documentation!

## To-Do
- Finish Jupyter Notebook documentation

## Authors

This is orginally based off of https://github.com/seemethere/nba_py so a lot of the work was done by those guys. My goal with this project is to clean up the code, add some proper documentation, and keep it up to date.
