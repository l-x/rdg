import unittest
from unittest import mock
from rdg import vocabulary
import random

class Vocabulary(unittest.TestCase):

    def setUp(self) -> None:
        self.dictionary = {
            "fu": [{
                "herp": "sna",
            }],
            "bar": [{
                "derp": "fu",
            }]
        }
        self.subject=vocabulary.Vocabulary(self.dictionary)

    @mock.patch('random.choice', side_effect=lambda v: v[0])
    def test_getRandomDict(self, choice_mock: mock.MagicMock) -> None:
        expected = {
            "herp": "sna",
            "derp": "fu",
        }

        self.assertEqual(self.subject.getRandomDict(), expected)

        self.assertEqual(choice_mock.call_count, len(self.dictionary))
