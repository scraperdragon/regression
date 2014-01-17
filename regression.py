function_type = type(lambda x: None)

def functions_of_class(cls):
    return dict((name, function) for name, function in cls.__dict__.items() if type(function) == function_type)

def tests_of_class(cls):
    return dict((name, function) for name in functions_of_class(x) if name[:5] == 'test_')
