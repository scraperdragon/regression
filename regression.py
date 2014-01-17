function_type = type(lambda x: None)


class DemoClass:
    pass
class_type = type(DemoClass)


def functions_of_class(cls):
    return dict((name, function) for name, function in cls.__dict__.items()
                if type(function) == function_type)


def tests_of_class(cls):
    return dict((name, cls.__dict__[name]) for name in functions_of_class(cls)
                if name[:5] == 'test_')


def classes_of_import(imp):
    return dict((name, cls) for name, cls in imp.__dict__.items() if type(cls) == type(type))
