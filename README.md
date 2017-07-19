# require
a small library to require python modules at runtime.

you can supply both a tuple with modulename and version or a single module name.

```from require import require_module

require_module(
  ("django", "1.8"),
  "reportlab",
)
```

enjoy!
