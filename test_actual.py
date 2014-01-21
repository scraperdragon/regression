import unittest
import helper

helper_suite = [['pass','a','a'], ['fail','a','b']]
TestSequence = helper.invoke(helper_suite)

def test_nope():
    pass
