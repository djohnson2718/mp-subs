
from string import digits


def popn(stack,n):
    l = [None]*n
    for i in range(n-1,-1,-1):
        l[i] = stack.pop()
    return l

wffVarsB = ["{p}","{s}","{x}","{t}"]
wffVars = "psxt"

aritys = {"ax-mp":4}

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
    return "R_" + s.replace("-","_")

def getSteps(codeString):
    i = 0
    l = []
    while i < len(codeString):
        bigdigits = []
        while codeString[i] in "UVWXY":
            bigdigits.append("UVWXY".index(codeString[i]) + 1)
            i += 1
        smalldigit = "ABCDEFGHIJKLMNOPQRST".index(codeString[i]) + 1
        bigdigits.reverse()
        l.append(smalldigit + sum((db*5**(j)*20 for j,db in enumerate(bigdigits)))-1)
        i += 1
    return l
    

def makeFunction(nVars, nHyp, refs, codeString, name):
    print("def " + name + "(" + ", ".join(wffVars[:nVars]) + (", " if nVars + nHyp > 0 else "") + ", ".join(("h" + str(i) for i in range(1,nHyp+1))) + "):")
    stack = []
    steps = getSteps(codeString)
    for i,s in enumerate(steps):
        #print(str(s))
        if s < nVars:
            stack.append(wffVarsB[s])
        elif s < nVars + nHyp:
            stack.append(Hyp(s - nVars + 1))
        else:
            ref = refs[s - nVars - nHyp]
            if ref == "wi":
                wffs = popn(stack,2)
                stack.append("." + str(wffs[0]) + str(wffs[1]))
            else:
                #assume it is a function
                arity = aritys[ref]
                pops = popn(stack, arity)
                params = ",".join(( f'f"{p}"' if isinstance(p, str) else str(p) for p in pops))

                print(f"    s{i} = {getFunctionName(ref)}({params})")
                stack.append(Step(i))
    aritys[name] = nVars + nHyp



makeFunction(3,3,["wi", "ax-mp"],"BCEABCGDFHH", "mp2")

makeFunction(3,3,["ax-mp"],"BCABDEGFG", "mp2d")

import re

l = re.findall(r"\$\{.*?\$\}", """
           $(
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
  Logical implication
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

  The results in this section are based on implication only, and avoid ~ ax-3 ,
  so are intuitionistic.  The system { ~ ax-mp , ~ ax-1 , ~ ax-2 } axiomatizes
  what is sometimes called "intuitionistic implicational calculus" or "minimal
  implicational calculus".

  In an implication, the wff before the arrow is called the "antecedent" and
  the wff after the arrow is called the "consequent".

$)

  ${
    mp2.1 $e |- ph $.
    mp2.2 $e |- ps $.
    mp2.3 $e |- ( ph -> ( ps -> ch ) ) $.
    $( A double modus ponens inference.  (Contributed by NM, 5-Apr-1994.) $)
    mp2 $p |- ch $=
      ( wi ax-mp ) BCEABCGDFHH $.
  $}

  ${
    mp2b.1 $e |- ph $.
    mp2b.2 $e |- ( ph -> ps ) $.
    mp2b.3 $e |- ( ps -> ch ) $.
    $( A double modus ponens inference.  (Contributed by Mario Carneiro,
       24-Jan-2013.) $)
    mp2b $p |- ch $=
      ( ax-mp ) BCABDEGFG $.
  $}

  ${
    a1i.1 $e |- ph $.
    $( Inference introducing an antecedent.  Inference associated with ~ ax-1 .
       Its associated inference is ~ a1ii .  See ~ conventions for a definition
       of "associated inference".  (Contributed by NM, 29-Dec-1992.) $)
    a1i $p |- ( ps -> ph ) $=
      ( wi ax-1 ax-mp ) ABADCABEF $.
  $}

  ${
    2a1i.1 $e |- ph $.
    $( Inference introducing two antecedents.  Two applications of ~ a1i .
       Inference associated with ~ 2a1 .  (Contributed by Jeff Hankins,
       4-Aug-2009.) $)
    2a1i $p |- ( ps -> ( ch -> ph ) ) $=
      ( wi a1i ) CAEBACDFF $.
  $}

  ${
    mp1i.1 $e |- ph $.
    mp1i.2 $e |- ( ph -> ps ) $.
    $( Inference detaching an antecedent and introducing a new one.
       (Contributed by Stefan O'Rear, 29-Jan-2015.) $)
    mp1i $p |- ( ch -> ps ) $=
      ( ax-mp a1i ) BCABDEFG $.
  $}""", re.DOTALL)


print(l)
