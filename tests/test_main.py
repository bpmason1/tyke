import unittest

from main import run
from unittest.mock import MagicMock, patch
from unittest.mock import call

class TestMain(unittest.TestCase):
    def test_run(self):
        all_directories = ['/foo', '/bar', '/baz', '/a/b/c']
        with patch('main.parseFile') as parseFileMock:
            with patch('main.processCode') as processCodeMock:
                run(all_directories)
                parse_file_calls = list(map(call, all_directories))
                parseFileMock.assert_has_calls(parse_file_calls)
                processCodeMock.assert_called_once()
