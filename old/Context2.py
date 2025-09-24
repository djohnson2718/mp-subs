from Parse6 import verify, match, subsFromDict, wffVars, StringWithCursor, peelWff

class Context2:
    def __init__(self):
        self.theorems = []
        self.theoremNumbers = {}
        self.namedTheorems = {}
        self.verbose = True
        self.contextName = ""

    def __getitem__(self, thmId):
        if isinstance(thmId, int):
            thm = self.theorems[thmId]
        else:
            thm = self.theorems[self.namedTheorems[thmId]]
        return thm
    
    def addAndGet(self, wff:str, message:str = None, name:str = None) -> int:
        newId = self.theoremNumbers.get(wff, None)
        if newId is None:
            newId = len(self.theorems)
            self.theorems.append(wff)
            self.theoremNumbers[wff] = newId
        if name != None:
            self.name(newId, name)
        if message != None:
            self.print(f"{self.contextName}{newId} ## {wff} [{message}]" + (f" ** {name}" if name is not None else ""))
        return newId

    def axiom(self, wff:str, name: str = None) -> int:
        verify(wff)
        thmId = self.addAndGet(wff, "Axiom", name)
        return thmId
    
    def name(self, thmId : int, name : str):
        self.namedTheorems[name] = thmId

    def subs(self, thmId, subsDict:dict, firstMatch:str = None, name:str = None)->int:
        if firstMatch != None:
            verify(firstMatch)
            firstSubs = match(self[thmId], firstMatch)
            targetStr = subsFromDict(self[thmId], firstSubs)
        else:
            targetStr = self[thmId]

        for k in subsDict.keys():
            if k not in wffVars:
                raise Exception(f"{k} is not a wff var")
        for v in subsDict.values():
            verify(v)

        newThm = subsFromDict(targetStr, subsDict)
        verify(newThm) #might be redundant, but lets be safe

        if firstMatch != None:
            message = f"[Subs {subsDict}->{firstSubs}->{thmId})]"
        else:
            message = f"[Subs {subsDict}->{thmId})]"

        return self.addAndGet(newThm, message, name)        
    
    def mp(self, antecedent, target, name:str = None)->int:
        st = StringWithCursor(self[target])
        if st[0] == '→':
            st.cursor+=1
            targetAnt = peelWff(st)
            if targetAnt == self[antecedent]:
                conclusion = peelWff(st)
                message = f"[Modus Ponens {antecedent}, {target}]"
                return self.addAndGet(conclusion, message, name)                
            else:
                raise Exception("antecedent does not match")
        else:
            raise Exception("Not an implication")
        
    def print(self, s : str):
        if self.verbose:
            print(s)