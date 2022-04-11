'''
The Record class models a database record as storage
for an ordered list of field names
whose values have types we don't care about.

While a dictionary is ideal for passing records around,
the mis-spelling of key names goes unnoticed by the interpreter,
so application code can be fragile
when record dicts are being constructed.

A dict with an immutable list of keys would be ideal for this.
Instead, Record.__slots__ is used here to restrict an object's attributes,
and Record.as_dict() is used to render the object as a dict
once it is constructed.

Referencing an attribute (either directly, or through keyword arguments)
that is not in __slots__ results in an AttributeError.
'''

class Record:
    '''
    >>> class MyRecord(Record):
    ...     __slots__ = ['a', 'b', 'c']

    >>> rec = MyRecord(a=1)
    >>> rec.b = 2
    >>> assert rec.a == 1 and rec.b == 2 and rec.c == None
    >>> rec.update(a='A', b='B')
    >>> assert dict(a='A', b='B', c='C') == rec.as_dict(c='C')
    >>> assert rec.a == 'A' and rec.b == 'B' and rec.c == None
    >>> rec.d = 1
    AttributeError: 'MyRecord' object has no attribute 'd'
    '''
    __slots__ = [] # Must provide a list of attribute names.

    def __init__(self, **kwargs):
        '''
        Initialize 0 or more attributes.
        Uninitialized attributes are set to None.
        '''
        for attr in self.__slots__:
            setattr(self, attr, None)
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def __str__(self):
        attrs = ', '.join(f'{a}={getattr(self, a)}' for a in self.__slots__)
        return f'<{self.__class__.__name__} {attrs}>'

    def as_dict(self, **kwargs) -> dict:
        '''
        Return self rendered as a dict, updated with any kwargs.
        Leaves self unchanged.
        '''
        self.__class__(**kwargs)    # validate kwargs
        dic = {attr: getattr(self, attr) for attr in self.__slots__}
        dic.update(kwargs)
        return dic

    def update(self, **kwargs):
        '''
        Update self from kwargs
        and (as a convenience for chaining) return self.
        '''
        self.__class__(**kwargs)    # validate kwargs
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self
