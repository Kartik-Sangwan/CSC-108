"""A3. Tester for the function extract_mentions in tweets.
"""

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    """Tester for the function extract_mentions in tweets.
    """

    def test_empty(self):
        """Empty tweet."""

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        """Non-empty tweet with no mentions."""

        arg = 'tweet test case'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
    
   
    def test_nonempty_multiple_mentions(self):
        """Non-empty tweet with multiple unique mentions."""

        arg = 'tweet @test and this @case lets @go'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'case', 'go']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)      
    
    def test_nonempty_multiple_same_mentions(self):
        """Non-empty tweet with multiple same mentions."""

        arg = 'tweet @test @test this @case lets @go meal.'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'test', 'case', 'go']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_nonempty_numeric_mentions(self):
        """Non-empty tweet with numeric multiple mentions and hastags."""

        arg = 'tweet @test23 and this @case lets #go and.'
        actual = tweets.extract_mentions(arg)
        expected = ['test23', 'case']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    def test_nonempty_nonalphanumeric_mention(self):
        """Non-empty tweet with multiple mentions with non alphanumeric."""

        arg = 'tweet @test #and this @cat$se lets @go'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'cat', 'go']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
    def test_nonempty_no_valid_mention(self):
        """Non-empty tweet with non valid mentions."""

        arg = 'tweet and this @! lets.'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_nonempty_case_sensitive_mentions(self):
        """Non-empty tweet with multiple mentions case sensitive."""

        arg = 'tweet @Test and this @caSE lets @go'
        actual = tweets.extract_mentions(arg)
        expected = ['test', 'case', 'go']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    


if __name__ == '__main__':
    unittest.main(exit=False)
