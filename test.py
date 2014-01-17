import regression
from nose.tools import assert_equal


class MyTestClass(object):

    def setUpTest(self):
        pass

    def test_function(self):
        pass


def test_get_functions():
    functions = regression.functions_of_class(MyTestClass)
    assert_equal(set(functions), set(['test_function', 'setUpTest']))
