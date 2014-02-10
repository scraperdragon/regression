import pickle
import helper


class TestNotFoundError(Exception):
    pass


def get_results(function):
    d = (function.__name__, function())
    return d


class Case(object):
    def set_up(self):
        self.run_these = []

    def __init__(self):
        self.set_up()
        self._filename = "pickled_tests"

    def save(self):
        """write all function data to file.
        This function should:
            * only be called when the diffs look good
            * confirm verify_from_file passes afterwards
        """
        output = {}
        for function in self.run_these:
            output.update(dict([get_results(function)]))
        self.export_to_file(output)
        self.verify_all_from_file()

    def all_tests(self):
        """Create nosetests test cases"""
        imported = self.import_from_file()
        builder = []
        for f in self.run_these:
            builder.append([f.__name__,
                           imported.get(f.__name__, TestNotFoundError),
                           f])
        return helper.invoke(builder)

    def verify_all_from_file(self):
        imported = self.import_from_file()
        """Run tests by comparing to previous output"""
        for f in self.run_these:
            name, result = get_results(f)
            try:
                assert imported[name] == result
            except KeyError:
                raise TestNotFoundError(name)

    def import_from_file(self):
        """
        Load past test data from file.
        See export_to_file for doctest.
        """
        with open(self._filename, 'r') as fobj:
            from_pickle = pickle.load(fobj)
            return from_pickle

    def export_to_file(self, to_pickle):
        """save current test data to file, as a pickle
        >>> case = Case()
        >>> case._filename = '__doctest_import'
        >>> Case().export_to_file([12, "ab"])
        >>> Case().import_from_file()
        [12, 'ab']
        """
        # TODO: protocol
        with open(self._filename, 'w') as fobj:
            pickle.dump(to_pickle, fobj, 2)
        return to_pickle
