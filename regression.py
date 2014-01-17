function_type = type(lambda x: None)

def functions_of_class(cls):
    return list(name for name, function in cls.__dict__.items() if type(function) == function_type)
