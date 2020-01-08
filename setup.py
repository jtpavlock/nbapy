from setuptools import setup

with open('README.md', 'r') as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='nbapy',
    version='1.1.0',
    description='Python client for NBA statistics located at nba.com',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/jtpavlock/nbapy',
    packages=[
        'nbapy',
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
