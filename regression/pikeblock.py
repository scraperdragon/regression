import pickle
import introspect
import helper


class TestNotFoundError(Exception):
    pass


class Case(object):
    def set_up(self):
        pass

    def __init__(self):
        self.filename = "pickled_tests"
        self.set_up()
        self.run_these = introspect.tests_of_instance(self)

    def save(self):
        """write all function data to file.
        This function should:
            * only be called when the diffs look good
            * confirm verify_from_file passes afterwards
        """
        output = {}
        for name, function in self.run_these.items():
            output.update({name: function()})
        self.export_to_file(output)
        self.verify_all_from_file()

    def all_tests(self):
        """Create nosetests test cases"""
        imported = self.import_from_file()
        builder = []
        for name, function in self.run_these.items():
            builder.append([name,
                           imported.get(name, TestNotFoundError),
                           function])
        return helper.invoke(builder)

    def verify_all_from_file(self):
        imported = self.import_from_file()
        """Run tests by comparing to previous output"""
        for name, function in self.run_these.items():
            try:
                assert imported[name] == function()
            except KeyError:
                raise TestNotFoundError(name)

    def import_from_file(self):
        """
        Load past test data from file.
        See export_to_file for doctest.
        """
        with open(self.filename, 'r') as fobj:
            from_pickle = pickle.load(fobj)
            return from_pickle

    def export_to_file(self, to_pickle):
        """save current test data to file, as a pickle
        >>> case = Case()
        >>> case.filename = '__doctest_import'
        >>> Case().export_to_file([12, "ab"])
        >>> Case().import_from_file()
        [12, 'ab']
        """
        # TODO: protocol
        with open(self.filename, 'w') as fobj:
            pickle.dump(to_pickle, fobj, 2)
        return to_pickle
