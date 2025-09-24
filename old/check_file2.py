from parse3 import CandidateFormula
map = {}

def axiom(name, wffString):
    c = CandidateFormula(wffString)
    if c.status == CandidateFormula.OK:
        map[name] = c
    else:
        raise Exception("Axiom is not a wff!")
    print(f'axiom("{name}", "{wffString}")')
    print("# " + str(c))

def subsWFF(name, target, wffVar, wffString, *setVars):
    c = map[target].subsWFF(wffVar, wffString, *setVars)
    map[name] = c
    print (f'subsWff("{name}", "{target}", "{wffVar}", "{wffString}", "{setVars}")')
    print("# " + str(c))

def mp(name, statement, ant):
    