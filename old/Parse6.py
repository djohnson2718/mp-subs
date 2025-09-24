import re
wffVars = '𝛼𝛽𝛾𝜒𝜓𝜑𝜃'

class InsertOnlyDict(dict):
    def __setitem__(self, key, value):
        if key in self and self[key] != value:
            raise KeyError(f"Key '{key}' already exists.")
        super().__setitem__(key, value)
    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v  # Will trigger __setitem__


class StringWithCursor(object):
    def __init__(self, string):
        self.string = string
        self.cursor = 0

    def __getitem__(self, i):
        return self.string[self.cursor+i]
    
    def end(self):
        return self.cursor >= len(self.string)
    
    def __repr__(self):
        return self.string[:self.cursor] + "*" + self.string[self.cursor:]
    

patterns = ['→ww','¬w','↔ww','⋀ww']

def peelWff(sc:StringWithCursor):
    if sc[0] in wffVars:
        result = sc[0]
        sc.cursor+=1
        return result
    for p in patterns:
        if p[0] == sc[0]:
            result = sc[0]
            sc.cursor += 1
            for t in p[1:]:
                if t=='w':
                    result += peelWff(sc)
                else:
                    raise Exception(f"patern {t} not implemented")
            return result
    raise Exception(f"Next character {sc[0]} not recognized")

def peelMatch(tc:StringWithCursor, sc:StringWithCursor, matchDict):
    if tc[0] in wffVars:
        matchDict[tc[0]] = peelWff(sc)
        tc.cursor += 1
        return
    for p in patterns:
        if p[0] == tc[0]:
            if p[0] != sc[0]:
                raise Exception(f"Match failed, {tc[0]} in target doesn't match {sc[0]} in source")
            sc.cursor+=1
            tc.cursor+=1
            for t in p[1:]:
                if t=='w':
                    peelMatch(tc,sc,matchDict)
                else:
                    raise Exception(f"patern {t} not implemented")
            return
    raise Exception(f"Next character {tc[0]} in target not recognized")

def verify(s:str):
    sc = StringWithCursor(s)
    peelWff(sc)
    if not sc.end():
        raise Exception(f"Parsing finished but string not consumed!")
    
def match(target:str, source:str):
    matchDict = InsertOnlyDict()
    sc = StringWithCursor(source)
    tc = StringWithCursor(target)
    peelMatch(tc, sc, matchDict)
    if not sc.end():
        raise Exception(f"Parsing finished but string not consumed!")
    return matchDict

class Context:
    def __init__(self, verbose = True):
        self.verbose = verbose
        self.theorems = {}

    def print(self, m):
        if self.verbose:
            print(m)

    def __getitem__(self, name):
        return self.theorems[name]

    def axiom(self, name:str, wff:str):
        verify(wff)
        self.theorems[name] = wff
        self.print(f"{wff} #{name} [Axiom] ")

    def alias(self, name:str, target:str):
        self.theorems[name] = self.theorems[target]
        self.print(f"{self.theorems[name]} #{name} [Alias for {target}]")

    def subs(self, name:str, target:str, subsDict:dict, firstMatch:str=None):
        if firstMatch != None:
            verify(firstMatch)
            firstSubs = match(self[target], firstMatch)
            targetStr = subsFromDict(self[target], firstSubs)
        else:
            targetStr = self[target]

        name = trimName(name)
        for k in subsDict.keys():
            if k not in wffVars:
                raise Exception(f"{k} is not a wff var")
        for v in subsDict.values():
            verify(v)

        newThm = subsFromDict(targetStr, subsDict)
        verify(newThm) #might be redundant, but lets be safe

        self.theorems[name] = newThm
        if firstMatch != None:
            self.print(f"{newThm} #{name} [Subs {subsDict}->{firstSubs}->{target})]")
        else:
            self.print(f"{newThm} #{name} [Subs {subsDict}->{target})]")

    def mp(self, name:str, antecedent:str, target:str):
        name = trimName(name)
        st = StringWithCursor(self.theorems[target])
        if st[0] == '→':
            st.cursor+=1
            targetAnt = peelWff(st)
            if targetAnt == self.theorems[antecedent]:
                conclusion = peelWff(st)
                self.theorems[name] = conclusion
                self.print(f"{conclusion} #{name} [Modus Ponens {antecedent}, {target}]")
            else:
                raise Exception("antecedent does not match")
        else:
            raise Exception("Not an implication")


def trimName(name):
    return re.sub(r'\~+$', '', name)

def subsFromDict(s:str, d:dict):
    if len(d)==0:
        return s
    pattern = re.compile('|'.join(d.keys()))
    return pattern.sub(lambda m : d[m.group(0)], s)

def composeSubsDict(d1:dict, d2:dict):
    d3 = dict()
    for k,v in d1.items():
        d3[k] = subsFromDict(v,d2)
    return d3