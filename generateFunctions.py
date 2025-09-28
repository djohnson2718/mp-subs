def popn(stack,n):
    l = [None]*n
    for i in range(n-1,-1,-1):
        l[i] = stack.pop()
    return l

wffVarsId = ["ph","ps","ch","th","ta","et","ze","si","rh","mu","la","ka"]

aritys = {"ax-mp":4, "ax-1":2, "ax-2":3, "ax-3":2, "df-bi":2, 'df-an':2}

class Operator:
    def __init__(self, symbol, mmString, arity):
        self.symbol = symbol
        self.arity = arity
        self.mmString = mmString

    def __repr__(self):
        return self.symbol
    
ops = {
    "wn" : Operator("¬", "wn", 1),
    "wi" : Operator("→", "wi", 2),
    "wb" : Operator("↔", "wb", 2),
    "wa" : Operator("⋀", "wa", 2),
    "wo" : Operator("∨", "wo", 2)
}

class Hyp:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return "h" + str(self.n)
class Step:
    def __init__(self, n):
        self.n = n

    def __repr__(self):
        return "s" + str(self.n)
    

def getFunctionName(s):
    return "R_" + s.replace("-","_").replace(".","_")

def getSteps(codeString):
    i = 0
    l = []
    while i < len(codeString):
        if codeString[i] == 'Z':
            l.append('Z')
            i += 1
            continue
        if codeString[i].isspace():
            i += 1
            continue
        bigdigits = []
        while codeString[i] in "UVWXY":
            bigdigits.append("UVWXY".index(codeString[i]) + 1)
            i += 1
        smalldigit = "ABCDEFGHIJKLMNOPQRST".index(codeString[i]) + 1
        bigdigits.reverse()
        l.append(smalldigit + sum((db*5**(j)*20 for j,db in enumerate(bigdigits)))-1)
        i += 1
    return l
    

def makeFunction(nVars, nHyp, refs, steps, name, writer=print):
    if nHyp == 0:
        writer(f'@Theorem({nVars}, "{name}")')
    writer("def " + getFunctionName(name) + "(" + ", ".join(wffVarsId[:nVars]) + (", " if nVars > 0 and nHyp > 0 else "") + ", ".join(("h" + str(i) for i in range(1,nHyp+1))) + "):")
    stack = []
    savedSteps = []
    #steps = getSteps(codeString)
    for i,s in enumerate(steps):
        if s == 'Z':
            savedSteps.append(stack[-1])
            continue
        #print(str(s))
        if s < nVars:
            stack.append("{" + wffVarsId[s] + "}")
        elif s < nVars + nHyp:
            stack.append(Hyp(s - nVars + 1))
        elif s < nVars + nHyp + len(refs):
            ref = refs[s - nVars - nHyp]
            if ref in ops:
                op = ops[ref]
                pops = popn(stack, op.arity)
                stack.append(op.symbol + "".join(pops))
            else:
                #assume it is a function
                arity = aritys[ref]
                pops = popn(stack, arity)
                params = ", ".join(( f'f"{p}"' if isinstance(p, str) else str(p) for p in pops))
                if i == len(steps)-1:
                    writer(f"    return {getFunctionName(ref)}({params})")
                else:   
                    writer(f"    s{i} = {getFunctionName(ref)}({params})")
                stack.append(Step(i))
        else:
            stack.append(savedSteps[s - nVars - nHyp - len(refs)])
    writer("")
    aritys[name] = nVars + nHyp

import re

with open("set.mm") as f:
    setmm = f.read(350000)

excludeNames = set([])

def parse(it, nHypsPrevLevel):
    nHypsThisLevel = 0
    while True:
        try:
            m = next(it)
        except StopIteration:
            return
        if m.group("startComment") != None:
            while m.group("endComment") == None:
                try:
                    m = next(it)
                except StopIteration:
                    return
        if m.group("start") != None:
            parse(it, nHypsPrevLevel + nHypsThisLevel)
        elif m.group("end") != None:
            return
        elif m.group("hyp") != None:
            nHypsThisLevel += 1
        elif m.group("ax") != None:
            pass #ignore axioms for now
        elif m.group("provableName") != None:
            codeString = m.group("code")
            refs = [r for r in m.group("refs").split(" ") if r != '']
            name = m.group("provableName")
            if name in excludeNames or name.endswith("ALT"):
                print("### Skipping: " + name)
                continue
            nHyp = nHypsPrevLevel + nHypsThisLevel
            print("#### Name: " + name)
            print("hyps "  + str(nHypsPrevLevel) + " + " + str(nHypsThisLevel) + " = " + str(nHyp))
            steps = getSteps(codeString)
            numStepLabels = max([st for st in steps if isinstance(st, int)]) + 1 - (steps.count('Z'))
            nVars = numStepLabels - nHyp - len(refs) 
            print("step labels " + str(numStepLabels))
            print("vars "  + str(nVars))
            print(codeString, steps)
            print(refs)
            makeFunction(nVars, nHyp, refs, steps, name, writer=lambda line : tl.write(line + "\n"))
            print("******")

ofInterest = re.compile(r"(?P<startComment>\$\()|(?P<endComment>\$\))|(?P<start>\$\{)|(?P<end>\$\})|(?P<hyp>\$e\s\|\-)|(?P<ax>\$a\s\|\-)|(?P<provableName>[\w\-\.]+)\s\$p\s\|\-.*?\$\=\s+\(\s(?P<refs>[\w\-\.\s]*?)\s\)\s+(?P<code>[A-Z\s]+)\s\$\.", re.DOTALL)
it = ofInterest.finditer(setmm)

with open("TrueLines.py", "w") as tl:
    tl.write("from header import *\n\n")
    parse(it, 0)
    tl.write(r'c.makePage("html/TrueLines.html")')

