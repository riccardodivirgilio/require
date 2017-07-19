# require
a small py2/py3 library to require python modules at runtime.

you can supply both a tuple with modulename and version or a single module name.

```python
from require import require_module

require_module(
    ("django", "1.8"),
    "reportlab",
)
```

enjoy!
