"""Test nba_api.py."""
import json

import pytest

from nbapy.nba_api import NbaAPI


class TestNbaAPI:
    """Test the API wrapper."""

    @staticmethod
    def test_connection():
        """Test basic connection to API without any endpoints."""
        with pytest.raises(json.JSONDecodeError):
            # this call doesn't return a json object, but if we got that far, we're good
            NbaAPI()
