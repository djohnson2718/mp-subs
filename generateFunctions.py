
from string import digits


def popn(stack,n):
    l = [None]*n
    for i in range(n-1,-1,-1):
        l[i] = stack.pop()
    return l

wffVarsId = ["ph","ps","ch","th","ta"]

aritys = {"ax-mp":4, "ax-1":2, "ax-2":3}

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
            if ref == "wi":
                wffs = popn(stack,2)
                stack.append("→" + wffs[0] + wffs[1])
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
codeStringPattern = re.compile(r"\$=\s*\((.*?)\)\s*([A-Z]+)\s*\$")
refsPattern = re.compile(r"\(\s([\sa-z0-9\-]+)\s\)")

with open("set.mm") as f:
    setmm = f.read(50000)

#print(setmm[-4500:])
l = re.findall(pattern, setmm)

count = 0
with open("TrueLines.py", "w") as tl:
    tl.write("from header import *\n\n")
    for s in l:
        count += 1
        if count < 10:
            continue
        print(s)
        nHyp = s.count("|-")-1
        nameSearchResult = namePattern.search(s)
        name = nameSearchResult.group(1)
        if name == '4syl' or name == 'idALT' or name == 'syl2im' or name == 'syl2imc':
            #syl2imc reused hypotheses
            continue
        print(name)
        print(nHyp)
        codeString = codeStringPattern.search(s).group(2)
        print(codeString)
        refsString = refsPattern.search(s).group(1)
        print(refsString)
        refs = [r for r in refsString.split(" ") if len(r)>0]
        print(refs)
        for i, v in enumerate(wffVarsId):
            if f" {v} " in s:
                nVars = i + 1
            else:
                break
        print("******")
        makeFunction(nVars, nHyp, refs, codeString, name, writer=lambda line : tl.write(line + "\n"))
        print()
    tl.write(r'c.makePage("html/TrueLines.html")')



