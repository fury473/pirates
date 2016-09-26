from collections import Iterable
from json import dumps
from pprint import pprint
from types import GeneratorType

def to_dict(model, max_depth=None):

    if isinstance(model,(type(None),str,int,float,bool)):
        return str(model)

    if max_depth != None and max_depth == 0:
        return str(type(model))

    depth = (max_depth - 1 if max_depth != None else None)

    if isinstance(model, (list, tuple)):
        repr = []
        for i, value in enumerate(model):
            repr.append(to_dict(value, depth))
        return tuple(repr) if isinstance(model, tuple) else repr
    elif isinstance(model, GeneratorType):
        return to_dict(list(model), depth)
    elif isinstance(model, dict):
        repr = {}
        for i, property in enumerate(model):
            value = model[property]
            repr[property] = to_dict(value, depth)
        return repr
    elif isinstance(model, Iterable):
        return to_dict(list(model))
    else:
        repr = {}
        for i, property in enumerate(vars(model)):
            value = eval('model.'+property)
            repr[property] = to_dict(value, depth)
        return repr

def debug(model, max_depth=None):
    pprint(to_dict(model, max_depth))

def json_debug(model, max_depth=None):
    print(dumps(to_dict(model, max_depth), sort_keys=True, indent=4))

