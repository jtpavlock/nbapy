from setuptools import setup

with open("README.md", "r") as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name="nbapy",
    version="1.1.4",
    description="Python client for NBA statistics located at nba.com",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/jtpavlock/nbapy",
    packages=["nbapy"],
    install_requires=["requests", "pandas"],
    extras_require={
        "dev": [
            "flake8",
            "flake8-bugbear",
            "flake8-docstrings",
            "mypy",
            "pre-commit",
            "pytest",
            "pytest-cov",
            "requests_cache",  # to speed up testing
        ]
    },
    python_requires=">=3.6",
)
