from nose.tools import assert_equal
import introspect
function_type = type(lambda x: None)

class MyTestClass(object):
    blah = 42

    @classmethod
    def setUpTest(self):
        pass

    def test_function(self):
        return self.blah

    def not_a_you_know_what(self):
        pass


def test_get_functions():
    functions = introspect.functions_of_class(MyTestClass)
    assert_equal(set(functions), set(['test_function', 'not_a_you_know_what']))
    assert type(functions['test_function']) == function_type


def test_get_tests():
    functions = introspect.tests_of_class(MyTestClass)
    assert_equal(set(functions), set(['test_function']))
    assert type(functions['test_function']) == function_type

def test_get_tests_of_instance():
    foo = MyTestClass()
    item, = list(introspect.tests_of_instance(foo).items())
    assert_equal(item[0], 'test_function')
    assert_equal(item[1](), 42)

