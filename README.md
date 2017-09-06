# require
a small py2/py3 library to require python modules at runtime.

modules will be installed using PIP.

you can supply both a tuple with modulename and version or a single module name.

```python
from require import require_module

require_module("django")
require_module(django = '1.8')
require_module(["django", '1.8'])
```

or you can use the decorator to require modules on function call

```
from require import require

@require('django')
def hello():
	import django
	print(django)

@require(django = 1.8)
def hello():
	import django
	print(django)

@require(["django", "1.8"])
def hello():
	import django
	print(django)
```

enjoy!
