#!/bin/python3

## https://pyobfuscate.com/pyd

class compile:
    def __init__(self):
        return
    def __call__(self, *args, **kwargs):
        print(eval(__import__('ast').unparse(args[0])[4:]))
        exit(0)

compile = compile()
__import__('builtins').compile = compile

file = open(input(">> input file path: "), 'rb').read()
print('>> source code: ')
exec(file)