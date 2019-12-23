# *nbapy - [stats.nba.com](https://stats.nba.com) API for python*

## Documentation
An ongoing process, but check out the [wiki](https://github.com/jtpavlock/nbapy/wiki), the [jupyter notebook docs](https://github.com/jtpavlock/nbapy/tree/master/docs/), or feel free to poke around the codebase.

## Summary
A python facing API for stats.nba.com (Still in heavy development)

## Installation
NOTE: Developmental builds, are by no means stable If you want the stable version use:

```
$ pip install nbapy
```

Else:
- Download from source (git clone, zipped package)
- Run from the root directory:

```
$ pip install .
```

## Requirements
- [requests](http://www.python-requests.org/en/latest/)
- [pandas](https://pandas.pydata.org/)

## Development
#### 1. Fork the repository and create a feature/bug fix branch

#### 2. Install development requirements
`$ pip install -e . ".[dev]"`

#### 3. Hack away
#### 4. Create some tests

#### 5. Make sure it's good code
`$ pytest --cov`

`$ flake8`

#### 6. Submit a pull request

Other ways to contribute involve submitting any issues or adding some documentation!

## To-Do
- Finish Jupyter Notebook documentation
