import importlib
import os

def _import_modules():
    for moduleName in sorted(
        os.path.splitext(filename)[0]
        for filename in os.listdir(os.path.dirname(__file__))
        if filename.endswith('.py') and filename not in ('__init__.py',)
    ):
        importlib.import_module(f'.{moduleName}', 'snscrape.modules')

_import_modules()
