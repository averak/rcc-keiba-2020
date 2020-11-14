import os
import glob

__all__ = []

for file in glob.glob(os.path.dirname(__file__) + '/attr_*.py'):
    module_name = os.path.basename(file).replace('.py', '')
    exec('import inspect')
    exec('from . import {}'.format(module_name))
    class_name = eval(
        'inspect.getmembers(%s, inspect.isclass)[0][0]' % module_name)
    exec('from .{} import {}'.format(module_name, class_name))
    __all__.append(class_name)
