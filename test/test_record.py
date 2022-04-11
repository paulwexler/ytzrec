import pytest

from ytzrec import record

class MyRecord(record.Record):
    __slots__ = ['a', 'b', 'c']

def test_record():
    rec = MyRecord(a=1)
    rec.b = 2
    assert rec.a == 1 and rec.b == 2 and rec.c == None
    rec.update(a='A', b='B')
    assert dict(a='A', b='B', c='C') == rec.as_dict(c='C')
    assert rec.a == 'A' and rec.b == 'B' and rec.c == None

def test_str():
    rec = MyRecord(a="Hello", b=1)
    result = str(rec)
    expect = '<MyRecord a=Hello, b=1, c=None>'
    assert result == expect

def test_exception():
    rec = MyRecord(a=1)
    with pytest.raises(AttributeError) as exc:
        rec.d = 1
    result = str(exc.value)
    expect = "'MyRecord' object has no attribute 'd'"
    assert result == expect
