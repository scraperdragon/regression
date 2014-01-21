# http://stackoverflow.com/questions/32899/generate-dynamic-unit-tests-python

import unittest

l = [["foo", "a", "a"],
     ["bar", "a", "b"],
     ["lee", "b", "b"]]


def _test_generator(a, b):
    def test(self):
        self.assertEqual(a, b)
    return test

def invoke(tests, test_class):
    for t in tests:
        test_name = 'test_%s' % t[0]
        test = _test_generator(t[1], t[2])
        setattr(test_class, test_name, test)
#    unittest.main()
