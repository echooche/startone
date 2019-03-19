import foo
import time
import sys

a = [1, 'python']
a = 'a string'

def func():
    a = 1
    b = 257
    print(a + b)

print(a)

if __name__ == '__main__':
    func()
    f = foo.add(1, 2)
    print(f)

    # print(foo.__dict__)
    # print(dir())
    print(sys.modules)
"""
a string
1552974942.5839
258
1552974942.583924
=1552974942.583932
3
1552974942.583943
"""