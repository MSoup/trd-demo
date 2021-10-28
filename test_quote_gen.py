import unittest
import sys
from get_data import getRandomJoke


class TestRandomQuoteGenerator(unittest.TestCase):
    def test_access_api_success(self):
        joke = getRandomJoke()
        self.assertEqual(joke["status"], 200)

    def test_can_get_quote(self):
        joke = getRandomJoke()
        self.assertEqual(type(joke["joke"]), str)

    def test_repeated_calls_different_quotes(self):
        """
        There are 660 total jokes, so 5 calls to this API should statistically give us at least 2 unique joke
        """
        quoteSet = set()
        for i in range(5):
            quoteSet.add(getRandomJoke()["joke"])
        self.assertEqual(len(quoteSet) > 1, True)


    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

class TestMyFunction(unittest.TestCase):
    def test_function_returns_dictionary(self):
        self.assertEqual(type(getRandomJoke()), dict)


if __name__ == '__main__':
    unittest.main()