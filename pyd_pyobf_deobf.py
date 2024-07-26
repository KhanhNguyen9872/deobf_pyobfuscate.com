#!/bin/python3

## https://pyobfuscate.com/pyd
# Stop do shit thing

class compile:
    def __init__(self):
        try:
            __import__('builtins').ㅤ = __import__('builtins').exec.ㅤ[0]
        except:
            __import__('builtins').ㅤ = __import__('builtins').exec

        for ㅤ in dir(__import__('builtins').compile):
            try:
                __import__('builtins').ㅤ("self.{0} = __import__('builtins').compile.{0}".format(str(ㅤ)), {'self': self})
            except AttributeError:
                pass
        self.ㅤ = [vars(__import__('builtins')).copy()['compile'], 0]
        self.__dir__ = self.ㅤ[0].__dir__
        try:
            __import__('shutil').rmtree("_compile")
        except:
            pass
        try:
            del __import__('builtins').ㅤ
        except:
            pass
        return None
    
    def __repr__(self):
        return str(self.ㅤ[0])

    def __call__(self, *args, **kwargs):
        print(eval(__import__('ast').unparse(args[0])[4:]))
        exit(0)

    @property
    def __dict__(self):
        return self.ㅤ[0].__dict__
    @property
    def __class__(self):
        return self.ㅤ[0].__class__

compile = compile()
__import__('builtins').compile = compile

file = open(input(">> input file path: "), 'rb').read()
print('>> source code: ')
exec(file)