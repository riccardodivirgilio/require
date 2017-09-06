# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from functools import wraps

import pip

def parse_module_spec(*spec):
    for module in spec:
        if isinstance(module, (tuple, list)):
            module, version = module
            yield (module, version)
        elif isinstance(module, dict):
            for module, version in module.items():
                yield module, version
        else:
            try:
                module, version = module.split('==')
                yield module, version
            except ValueError:
                yield module, None

def installed_modules():
    return {
        i.key: i.version
        for i in pip.get_installed_distributions()
    }

def missing_requirements(*module_args, **modules_kw):

    distributions = installed_modules()

    for module, version in parse_module_spec(modules_kw, *module_args):

        if not module in distributions or version and not distributions[module] == version:
            yield version and "%s==%s" % (module, version) or module

def require_module(*module_args, **modules_kw):

    commands = list(missing_requirements(*module_args, **modules_kw))

    if commands:
        from pip.locations import virtualenv_no_global

        print("Update in progress: pip install %s --user" % " ".join(commands))

        if virtualenv_no_global():
            pip.main(["install"] + commands)
        else:
            pip.main(["install", "--user"] + commands)

def require(*module_args, **modules_kw):
    def outer(func):
        @wraps(func)
        def inner(*args, **kw):
            require_module(*module_args, **modules_kw)
            return func(*args, **kw)
        return inner
    return outer