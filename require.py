# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

import pip

def installed_modules():
    return {
        i.key: i.version
        for i in pip.get_installed_distributions()   
    }

def missing_requirements(*modules):

    if modules:
        distributions = installed_modules()

        for module in modules:
            version = None
            if isinstance(module, (tuple, list)):
                module, version = module

            if not module in distributions or version and not distributions[module] == version:
                yield version and "%s==%s" % (module, version) or module

def require_module(*modules):

    commands = list(missing_requirements(*modules))

    if commands:
        from pip.locations import virtualenv_no_global

        print("Update in progress: pip install %s --user" % " ".join(commands))

        if virtualenv_no_global():
            pip.main(["install"] + commands)
        else:
            pip.main(["install", "--user"] + commands)
