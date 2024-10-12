import inspect
def introspection_info(obj):
    type_ = type(obj)
    attribute = getattr(obj, '__dict__', None)
    methods = dir(obj)
    module = obj.__class__.__module__
    func = inspect.isfunction(obj)
    res = {'type': type_, 'attributes': attribute, 'methods': methods, 'module': module, 'function': func}
    return res

number_info = introspection_info(42)
print(number_info)
