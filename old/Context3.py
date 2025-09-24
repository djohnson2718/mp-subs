from Parse6 import verify, match, subsFromDict, wffVars, StringWithCursor, peelWff, composeSubsDict
from dataclasses import dataclass

class Proof:
    pass

class Theorem:
    def __init__(self, id :int , wff:str, proof:Proof):
        self.id = id
        self.wff = wff
        self.proof = proof
        self.names = []

    def __hash__(self):
        return hash(self.wff)
    
    def __eq__(self, other):
        return self.wff == other.wff
    
    def __str__(self):
        return f"{self.id} ## {self.wff} [{self.proof}] ** {self.names}"
    
    def html(self):
        namesStr = ", ".join(self.names)
        classes = []
        if len(self.names) > 0:
            classes.append("named")
        classes.append(self.proof.htmlClass())
        classStr = " ".join(classes)
        return f'<tr id = {self.id} {self.proof.htmlRefs()} class = "{classStr}" ><td>{self.id}</td><td>{self.wff}</td><td>{self.proof}</td><td>{namesStr}</td></tr>'
    
@dataclass
class ModusPonensProof(Proof):
    antecedentId : int
    targetId : int

    def __str__(self):
        return f"Modus ponens {self.antecedentId}, {self.targetId}"
    
    def htmlRefs(self):
        return f'antecedent = "{self.antecedentId}" mp-target = "{self.targetId}"'
    
    def htmlClass(self):
        return "mp"

@dataclass
class SubstiutionProof(Proof):
    targetId : int
    subsDict : dict

    def __str__(self):
        s = ", ".join([k + '↗' + v for k,v in self.subsDict.items() if not k == v])
        return f"Subs [{s}] into {self.targetId}"
    
    def htmlRefs(self):
        return f'sub-target = "{self.targetId}"'
    
    def htmlClass(self):
        return "subs"

class Axiom(Proof):
    def __str__(self):
        return "Axiom"
    def htmlRefs(self):
        return ""
    def htmlClass(self):
        return "axiom"

class Context3:
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
    
    def addAndGet(self, wff:str, proof : Proof) -> int:
        newId = self.theoremNumbers.get(wff, None)
        if newId is None:
            newId = len(self.theorems)
            newThm = Theorem(newId, wff, proof)
            self.theorems.append(newThm)
            self.theoremNumbers[wff] = newId
            self.print(newThm)
        return newId

    def axiom(self, wff:str) -> int:
        verify(wff)
        thmId = self.addAndGet(wff, Axiom())
        return thmId
    
    def name(self, thmId : int, name : str) -> int:
        self.namedTheorems[name] = thmId
        self[thmId].names.append(name)
        self.print(f"{thmId} -> {name}")
        return thmId

    def subs(self, thmId, subsDict:dict, firstMatch:str = None)->int:
        if isinstance(thmId, str):
            thmId = self.namedTheorems[thmId]

        if firstMatch != None:
            verify(firstMatch)
            firstSubs = match(self[thmId].wff, firstMatch)
            subsDict = composeSubsDict(firstSubs, subsDict)

        for k in subsDict.keys():
            if k not in wffVars:
                raise Exception(f"{k} is not a wff var")
        for v in subsDict.values():
            verify(v)

        newThm = subsFromDict(self[thmId].wff, subsDict)
        verify(newThm) #might be redundant, but lets be safe

        return self.addAndGet(newThm, SubstiutionProof(thmId, subsDict))

    def mp(self, antecedent, target)->int:
        if isinstance(antecedent, str):
            antecedent = self.namedTheorems[antecedent]
        if isinstance(target, str):
            target = self.namedTheorems[target]

        st = StringWithCursor(self[target].wff)
        if st[0] == '→':
            st.cursor+=1
            targetAnt = peelWff(st)
            if targetAnt == self[antecedent].wff:
                conclusion = peelWff(st)
                return self.addAndGet(conclusion, ModusPonensProof(antecedent, target))               
            else:
                raise Exception("antecedent does not match")
        else:
            raise Exception("Not an implication")
        
    def print(self, s : str):
        if self.verbose:
            print(self.contextName + str(s))

    def makePage(self, filename):
        with open(filename,"w", encoding="utf-8") as f:
            f.write(self.html())

    def html(self):
        return """
        <!DOCTYPE HMTL>
        <head>
            <title>Theorems</title>
            <link rel="stylesheet" type="text/css" href="tablestyle.css">
            <script src="highlight-ref.js" defer></script>
        </head>
        <body>
            <table>
                <thead><tr><th>Id</th><th>Statement</th><th>Proof</th><th>Names</th></tr></thead>
                <tbody>
        """ + \
       "            " + "\n".join((t.html() for t in self.theorems)) + """
                </tbody>
            </table>
        </body>"""
