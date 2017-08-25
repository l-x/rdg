import unittest
from unittest import mock
from rdg import jinja


class Jinja(unittest.TestCase):

    @mock.patch('jinja2.Environment')
    def test_environment_returns_jinja2_environment(self, mock_environment: mock.MagicMock) -> None:
        environment=mock_environment.return_value
        self.assertIs(jinja.environment(), environment)

        environment.filters.update.assert_called_once_with(jinja.custom_filters)
        environment.globals.update.assert_called_once_with(jinja.custom_globals)

