import inspect
from functools import wraps


def strict(func):
    signature = inspect.signature(func)
    parameters = signature.parameters

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            expected = parameters[name].annotation

            if expected is not inspect.Parameter.empty and not isinstance(value, expected):
                raise TypeError(f"Argument '{name}' must be of type {expected}, got {type(value)}")

        return func(*args, **kwargs)
    return wrapper
