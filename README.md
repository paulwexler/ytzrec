# ytsrec (it's rec) Model a database record.

## class Record

The Record class models a database record as storage
for an ordered list of field names
whose values have types we don't care about.

While a dictionary is ideal for passing records around,
the mis-spelling of key names goes unnoticed by the interpreter,
so application code can be fragile
when record dicts are being constructed.
A dict with an immutable list of keys would be ideal for this,
but the entire dict interface is not actually required.

Instead, `Record.__slots__` is used here to restrict an object's attributes,
and `Record.as_dict()` is used to render the object as a dict
once it is constructed.  `Record.update(**kwargs)` is provided
as a convenience to update several attributes at once.

Referencing an attribute (either directly, or through keyword arguments)
that is not in `__slots__` results in an `AttributeError`.

```python
from ytzrec import record

class MyRecord(record.Record):
    __slots__ = ['a', 'b', 'c']

rec = MyRecord(a=1)
rec.b = 2
assert rec.a == 1 and rec.b == 2 and rec.c == None
rec.update(a='A', b='B')
assert dict(a='A', b='B', c='C') == rec.as_dict(c='C')
assert rec.a == 'A' and rec.b == 'B' and rec.c == None
rec.d = 1
AttributeError: 'MyRecord' object has no attribute 'd'
```

## Installation

    pip install ytzrec

## Maintenance

    cd ytzrec
    pip install -e .
    pylint src/ytzrec/*.py # expect 10.00/10
    coverage erase
    coverage run source=src/ytzrec -m pytest -v test # expect all tests PASS
    coverage report -m # expect 100% coverage
