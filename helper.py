# http://stackoverflow.com/questions/32899/generate-dynamic-unit-tests-python

import unittest

class TestSequence(unittest.TestCase):
    pass

def _test_generator(static, function):
    def test(self):
        self.assertEqual(static, function())
    return test

def invoke(tests):
    for t in tests:
        test_name = 'test_%s' % t[0]
        test = _test_generator(t[1], t[2])
        setattr(TestSequence, test_name, test)
    return TestSequence
