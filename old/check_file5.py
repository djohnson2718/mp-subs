from parse5 import parseWff
import inspect
map={}

def axiom(name, wffString):
    print_function_call()
    newTheorem(name, parseWff(wffString))

def alias(name, existingName):
    print_function_call()
    newTheorem(name, map[existingName])

def setSub(name, target, setString):
    print_function_call()
    newTheorem(name, map[target].setSub(setString))

def wffSub(name, target, wffString, newWff):
    print_function_call()
    newTheorem(name, parseWff(map[target].wffSub(wffString, newWff)))

def modusPonens(name, target, antecedent):
    print_function_call()
    newTheorem(name, map[target].modusPonens(map[antecedent]))

def print_function_call():
    frame = inspect.currentframe().f_back
    func_name = frame.f_code.co_name
    args, _, _, values = inspect.getargvalues(frame)
    
    formatted_args = ', '.join(f'{arg}={repr(values[arg])}' for arg in args)
    print(f'{func_name}({formatted_args})')

def newTheorem(name, w):
    map[name] = w
    print('# ' + name)
    print('## ' + str(w))
    print()
