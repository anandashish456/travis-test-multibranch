from unittest import TestCase
from unittest.mock import patch
import src.call_api


class TestCall(TestCase):
    def test_res(self):
        with patch('src.call_api.requests.get') as mocked_call:
            src.call_api.call_google()
            mocked_call.assert_called_with('https://www.google.com')
