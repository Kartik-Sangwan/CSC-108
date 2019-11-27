"""A3. Tester for the function common_words in tweets.
"""

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    """Tester for the function common_words in tweets.
    """

    def test_empty(self):
        """Empty dictionary."""

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        """Dictionary with one word."""

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)

        
    def test_more_word_limit(self):
        """Dictionary with n words all remain."""

        arg1 = {'hello': 2, 'bye': 3, 'night': 12}
        arg2 = 3
        exp_arg1 = {'hello': 2, 'bye': 3, 'night': 12}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    
    
    def test_remove_some(self):
        """Dictionary with some same value for words not to be included."""

        arg1 = {'frosst': 4, 'google': 3, 'brain': 3, 'researcher': 5, 'by': 1}
        arg2 = 3
        exp_arg1 = {'frosst': 4, 'researcher': 5}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    
    
    def test_remove_all(self):
        """Dictionary with all same value for words none included."""

        arg1 = {'frosst': 3, 'google': 3, 'brain': 3, 'researcher': 3, 'by': 3}
        arg2 = 3
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)  
        
        
if __name__ == '__main__':
    unittest.main(exit=False)
