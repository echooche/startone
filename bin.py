s = open('demo1.py').read()
co = compile(s, 'demo1.py', 'exec')
import dis
dis.dis(co)


"""
 1            0 LOAD_CONST               0 (0)
              2 LOAD_CONST               1 (None)
              4 IMPORT_NAME              0 (foo)
              6 STORE_NAME               0 (foo)

  3           8 LOAD_CONST               2 (1)
             10 LOAD_CONST               3 ('python')
             12 BUILD_LIST               2
             14 STORE_NAME               1 (a)

  4          16 LOAD_CONST               4 ('a string')
             18 STORE_NAME               1 (a)

  6          20 LOAD_CONST               5 (<code object func at 0x10cc3e780, file "demo1.py", line 6>)
             22 LOAD_CONST               6 ('func')
             24 MAKE_FUNCTION            0
             26 STORE_NAME               2 (func)

 11          28 LOAD_NAME                3 (print)
             30 LOAD_NAME                1 (a)
             32 CALL_FUNCTION            1
             34 POP_TOP

 13          36 LOAD_NAME                4 (__name__)
             38 LOAD_CONST               7 ('__main__')
             40 COMPARE_OP               2 (==)
             42 POP_JUMP_IF_FALSE       70

 14          44 LOAD_NAME                2 (func)
             46 CALL_FUNCTION            0
             48 POP_TOP

 15          50 LOAD_NAME                0 (foo)
             52 LOAD_METHOD              5 (add)
             54 LOAD_CONST               2 (1)
             56 LOAD_CONST               8 (2)
             58 CALL_METHOD              2
             60 STORE_NAME               6 (f)

 16          62 LOAD_NAME                3 (print)
             64 LOAD_NAME                6 (f)
             66 CALL_FUNCTION            1
             68 POP_TOP
        >>   70 LOAD_CONST               1 (None)
             72 RETURN_VALUE

Disassembly of <code object func at 0x10cc3e780, file "demo1.py", line 6>:
  7           0 LOAD_CONST               1 (1)
              2 STORE_FAST               0 (a)

  8           4 LOAD_CONST               2 (257)
              6 STORE_FAST               1 (b)

  9           8 LOAD_GLOBAL              0 (print)
             10 LOAD_FAST                0 (a)
             12 LOAD_FAST                1 (b)
             14 BINARY_ADD
             16 CALL_FUNCTION            1
             18 POP_TOP
             20 LOAD_CONST               0 (None)
             22 RETURN_VALUE


"""