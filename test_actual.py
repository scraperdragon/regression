import unittest
import helper

class TestSequence(unittest.TestCase):
    pass

helper_suite = [['pass','a','a'], ['fail','a','b']]
helper.invoke(helper_suite, TestSequence)

def test_nope():
    pass
