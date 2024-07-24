#!/bin/python3

## https://pyobfuscate.com/pyd

class compile:
    def __init__(self):
        self.com = vars(__import__('builtins')).copy()['compile']

    def __call__(self, *args, **kwargs):
        p = __import__('ast').unparse(args[0])
        print(eval(p[4:]))
        exit(0)

compile = compile()
__import__('builtins').compile = compile

file = open(input(">> input file path: "), 'rb').read()

print('>> source code: ')
exec(file)