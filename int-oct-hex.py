Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:37:30) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========================== RESTART: C:/Test/btest.py ==========================
>>> a=b=c=100
>>> a,b,c
(100, 100, 100)
>>> a,b,c = 5,3.2,'hello'
>>> a,b,c
(5, 3.2, 'hello')
>>> 0o15
13
>>> 'A'
'A'
>>> '\101'
'A'
>>> '\x41'
'A'
>>> \n
SyntaxError: unexpected character after line continuation character
>>> str ='Hellow python'
>>> str
'Hellow python'
>>> str[0]
'H'
>>> str[2:]
'llow python'
>>> str[:]
'Hellow python'
>>> str*2
'Hellow pythonHellow python'
>>> str+'test'
'Hellow pythontest'
>>> str[-1:]
'n'
>>> str[-6:]
'python'
>>> dir
<built-in function dir>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'a1', 'b', 'b1', 'c', 'c1', 'str']
>>> del a
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a1', 'b', 'b1', 'c', 'c1', 'str']
>>> dir(builtins)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    dir(builtins)
NameError: name 'builtins' is not defined
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> True
True
>>> False
False
>>> int(True)
1
>>> int(False)
0
>>> int(97.9)
97
>>> int('100', 16)
256
>>> int('101010',2)
42
>>> float(90)
90.0
>>> float('90')
90.0
>>> float('67.99')
67.99
>>> hex(100)
'0x64'
>>> oct(100)
'0o144'
>>> 7J
7j
>>> type(7J)
<class 'complex'>
>>> 1+7.45j
(1+7.45j)
>>> complex()
0j
>>> complex(-4.04+0j)
(-4.04+0j)
>>> 
>>> print(10/2)
5.0
>>> print(10//2)
5
>>> print(10%3)
1
>>> print(divmod(10.3))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(divmod(10.3))
TypeError: divmod expected 2 arguments, got 1
>>> print(divmod(10,3))
(3, 1)
>>> 
>>> 
>>> a=10;
>>> b=2;
>>> a&b
2
>>> a|b
10
>>> a^b
8
>>> a<<1
20
>>> a>>1
5
>>> ~a
-11
>>> 
>>> 
>>> list1 = list(range(100))
>>> print(list1[2])
2
>>> print(list1[12:48:2])
[12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46]
>>> 
>>> 
>>> list2=[0,2,3,4,5]
>>> print(3 in list2)
True
>>> print(1 not in list2)
True
>>> m_oct = 100
>>> m_oct
100
>>> 
>>> 
>>> m_int = 100
>>> m_oct = 0o100
>>> m_hex = 0x100
>>> m_int, m_oct, m_hex
(100, 64, 256)
>>> m_int=int(100)
>>> m_int
100
>>> m_oct=int(100)
>>> m_oct
100
>>> m_oct=oct(100)
>>> m_oct
'0o144'
>>> m_hex=hex(100)
>>> m_hex
'0x64'
>>> 