
from string import digits


def popn(stack,n):
    l = [None]*n
    for i in range(n-1,-1,-1):
        l[i] = stack.pop()
    return l

wffVarsId = ["ph","ps","ch","th"]

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
    print("def " + name + "(" + ", ".join(wffVarsId[:nVars]) + (", " if nVars + nHyp > 0 else "") + ", ".join(("h" + str(i) for i in range(1,nHyp+1))) + "):")
    stack = []
    steps = getSteps(codeString)
    for i,s in enumerate(steps):
        #print(str(s))
        if s < nVars:
            stack.append("{" + wffVarsId[s] + "}")
        elif s < nVars + nHyp:
            stack.append(Hyp(s - nVars + 1))
        else:
            ref = refs[s - nVars - nHyp]
            if ref == "wi":
                wffs = popn(stack,2)
                stack.append("→" + wffs[0] + wffs[1])
            else:
                #assume it is a function
                arity = aritys[ref]
                pops = popn(stack, arity)
                params = ", ".join(( f'f"{p}"' if isinstance(p, str) else str(p) for p in pops))

                print(f"    s{i} = {getFunctionName(ref)}({params})")
                stack.append(Step(i))
    aritys[name] = nVars + nHyp



#makeFunction(3,3,["wi", "ax-mp"],"BCEABCGDFHH", "mp2")

#makeFunction(3,3,["ax-mp"],"BCABDEGFG", "mp2d")

import re
pattern = re.compile(r"\$\{(.*?)\$\}", re.DOTALL)

for i, s in enumerate(pattern.finditer("")):
    pass

l = re.findall(pattern, """
                 $( Axiom _Simp_.  Axiom A1 of [Margaris] p. 49.  One of the 3 axioms of
     propositional calculus.  The 3 axioms are also given as Definition 2.1 of
     [Hamilton] p. 28.  This axiom is called _Simp_ or "the principle of
     simplification" in _Principia Mathematica_ (Theorem *2.02 of
     [WhiteheadRussell] p. 100) because "it enables us to pass from the joint
     assertion of ` ph ` and ` ps ` to the assertion of ` ph ` simply".  It is
     Proposition 1 of [Frege1879] p. 26, its first axiom.  (Contributed by NM,
     30-Sep-1992.) $)
  ax-1 $a |- ( ph -> ( ps -> ph ) ) $.

  $( Axiom _Frege_.  Axiom A2 of [Margaris] p. 49.  One of the 3 axioms of
     propositional calculus.  It "distributes" an antecedent over two
     consequents.  This axiom was part of Frege's original system and is known
     as _Frege_ in the literature; see Proposition 2 of [Frege1879] p. 26.  It
     is also proved as Theorem *2.77 of [WhiteheadRussell] p. 108.  The other
     direction of this axiom also turns out to be true, as demonstrated by
     ~ pm5.41 .  (Contributed by NM, 30-Sep-1992.) $)
  ax-2 $a |- ( ( ph -> ( ps -> ch ) ) -> ( ( ph -> ps ) -> ( ph -> ch ) ) ) $.

  $( Axiom _Transp_.  Axiom A3 of [Margaris] p. 49.  One of the 3 axioms of
     propositional calculus.  It swaps or "transposes" the order of the
     consequents when negation is removed.  An informal example is that the
     statement "if there are no clouds in the sky, it is not raining" implies
     the statement "if it is raining, there are clouds in the sky".  This axiom
     is called _Transp_ or "the principle of transposition" in _Principia
     Mathematica_ (Theorem *2.17 of [WhiteheadRussell] p. 103).  We will also
     use the term "contraposition" for this principle, although the reader is
     advised that in the field of philosophical logic, "contraposition" has a
     different technical meaning.  (Contributed by NM, 30-Sep-1992.)  Use its
     alias ~ con4 instead.  (New usage is discouraged.) $)
  ax-3 $a |- ( ( -. ph -> -. ps ) -> ( ps -> ph ) ) $.
               
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
  $}""")

namePattern = re.compile(r"([\w\-]+)\s+\$p\s+\|-")
codeStringPattern = re.compile(r"\$=\s*\((.*?)\)\s*([A-Z]+)\s*\$")
refsPattern = re.compile(r"\(([\sa-z0-9\-]+)\)")
for s in l:
    nHyp = s.count("|-")-1
    print(nHyp)
    nameSearchResult = namePattern.search(s)
    name = nameSearchResult.group(1)
    print(name)
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
    
    makeFunction(nVars, nHyp, refs, codeString, name)




