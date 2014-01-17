import regression
import example_tests
from nose.tools import assert_equal


class MyTestClass(object):

    @classmethod
    def setUpTest(self):
        pass

    def test_function(self):
        pass

    def not_a_you_know_what(self):
        pass


def test_get_functions():
    functions = regression.functions_of_class(MyTestClass)
    assert_equal(set(functions), set(['test_function', 'not_a_you_know_what']))

def test_get_functions_from_example():
    functions = regression.functions_of_class(example_tests.ConvertTest)
    assert_equal(set(functions), set([
        'not_a_you_know_what',
        'test_sector',
        'test_caption_detail_always_total',
        'test_first_row',
        'test_commodities',
        'test_last_row',
        'test_measure',
        'test_indicator',
        'test_frequency_always_annual',
        'test_all_figures_are_floats',
        'test_dates',
        'test_correct_number_of_rows',
        'test_origin',
        'test_source']))
