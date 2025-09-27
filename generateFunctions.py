def popn(stack,n):
    l = [None]*n
    for i in range(n-1,-1,-1):
        l[i] = stack.pop()
    return l

wffVarsId = ["ph","ps","ch","th","ta","et"]

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
    

def makeFunction(nVars, nHyp, refs, codeString, name, writer=print):
    if nHyp == 0:
        writer(f'@Theorem({nVars}, "{name}")')
    writer("def " + getFunctionName(name) + "(" + ", ".join(wffVarsId[:nVars]) + (", " if nVars > 0 and nHyp > 0 else "") + ", ".join(("h" + str(i) for i in range(1,nHyp+1))) + "):")
    stack = []
    savedSteps = []
    steps = getSteps(codeString)
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



#makeFunction(3,3,["wi", "ax-mp"],"BCEABCGDFHH", "mp2")

#makeFunction(3,3,["ax-mp"],"BCABDEGFG", "mp2d")

import re
pattern = re.compile(r"\$\{.*?\$\}|[\w\-\.]+\s\$p.*?\$\.", re.DOTALL)
namePattern = re.compile(r"([\w\-\.]+)\s\$p\s\|-")
codeStringPattern = re.compile(r"\$=\s*\((.*?)\)\s*([A-Z\s]+)\s\$\.")
refsPattern = re.compile(r"\(\s([\sa-z0-9\-\.]+)\s\)")

p = re.compile(r"[\w\-\.]+\s\$e\s\|\-\s(?P<hyp>.*?)\s\$.|(?P<name>[\w\-\.]+)\s\$p\s\|\-\s(?P<provable>.*?)\s\$\=\s+\(\s(?P<refs>.*?)\s\)\s(?P<code>[A-Z\s]+)\s\$\.", re.DOTALL)


def countVars(hyps):
    nVars = 0
    for v in wffVarsId:
        for h in hyps:
            if v in h:
                nVars += 1
                break
    return nVars

with open("set.mm") as f:
    setmm = f.read(200000)

l = re.findall(pattern, setmm)
excludeNames = set([])
count = 0
with open("TrueLines.py", "w") as tl:
    tl.write("from header import *\n\n")
    for s in l:
        count += 1
        if count < 8:
            continue
        print("s= \n" + s)
        hyps = []
        for m in p.finditer(s):
            if m.group("hyp") != None:
                hyps.append(m.group("hyp"))
                continue
            print (hyps)
            if m.group("provable") != None:
                codeString = m.group("code")
                refs = m.group("refs").split(" ")
                nHyp = len(hyps)
                nVars = countVars(hyps + [m.group("provable")])
                name = m.group("name")
                if name in excludeNames or name.endswith("ALT"):
                    print("### Skipping: " + name)
                    continue
                print("#### Name: " + name)
                print("hyps "  + str(nHyp))
                print("vars "  + str(nVars))
                print(codeString)
                print(refs)
                makeFunction(nVars, nHyp, refs, codeString, name, writer=lambda line : tl.write(line + "\n"))
                print("******")
                
        print()
    tl.write(r'c.makePage("html/TrueLines.html")')



