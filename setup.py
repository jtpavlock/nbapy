from distutils.core import setup

with open('README.md', 'r') as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='nba_stats',
    version='1.0.1',
    description='Python client for NBA statistics located at nba.com',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/jtpavlock/nba_stats',
    packages=[
        'nba_stats',
    ],
    install_requires=[
        'requests',
        'pandas',
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'requests_cache',  # to speed up testing
            'flake8',
        ]
    },
    python_requires='>=3.6',
)
