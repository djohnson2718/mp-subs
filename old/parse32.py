wffVars = '𝛼𝛽𝛾𝜒𝜓𝜑'
setVars = 'tuvwxyz'
subVars = "TUVWXYZ"

class CandidateFormula(object):
    
    IN_PROGRESS = 1
    INVALID = 0
    OK = 2

    def __init__(self, s):
        self.s = s
        self.cursor = 0
        self.var_map = dict()
        self.status = CandidateFormula.IN_PROGRESS
        self.wff_arg_counts = dict()
        self.parameterized_wffs = dict()
        self.subs_vars = []
        self.peelWFF("")
        if self.status == CandidateFormula.IN_PROGRESS and self.cursor == len(s):
            self.status = CandidateFormula.OK
        elif self.status == CandidateFormula.IN_PROGRESS and self.cursor < len(s):
            self.error_message = "Expected end of formula"
            self.status = CandidateFormula.INVALID

    def __getitem__(self, i):
        return self.s[self.cursor+i]
    
    def remaining(self):
        return len(self.s) - self.cursor
    
    def __repr__(self) -> str:
        return self.s[:self.cursor] + "*" + self.s[self.cursor:]
    
    def peelWFF(self, vars, leading = False):
        if self.status != CandidateFormula.IN_PROGRESS:
            return ""
        self.var_map[self.cursor] = vars
        if self.remaining()==0:
            self.error_message = "Expected: a wff. Got: end of formula."
            self.status = CandidateFormula.INVALID
        elif self[0] in wffVars:
            if self.remaining() == 1 or self[1] != '(':
                self.cursor+=1
                return self[-1]
            else:
                wffVar = self[0]
                self.cursor += 1
                setList = SetList(self, "(",")",",", vars)
                if self.status == CandidateFormula.INVALID:
                    return ""
                lists = self.parameterized_wffs.get(wffVar)
                if lists == None:
                    lists = []
                    self.parameterized_wffs[wffVar] = lists
                else:
                    if len(setList.sets) != len(lists[0].sets):
                        self.error_message = f"The wff var {wffVar} previously had {len(lists[0].sets)} parameters, but now has {len(setList.sets)}"
                        self.status = CandidateFormula.INVALID
                        return ""
                lists.append(setList)
                return wffVar + setList.str

        elif self[0] == '∈' or self[0] == '=':
            self.cursor+=1
            return self[-1] + self.peelSet(vars) + self.peelSet(vars)
        elif self[0] == '𝜑':
            self.cursor+=1
            return self[-1] + self.peelWFF(vars) +  self.peelWFF(vars)
        elif self[0] == '¬':
            self.cursor+=1
            return self[-1] + self.peelWFF(vars)
        elif self[0] == '∀':
            if self[1] in setVars and self[1] not in vars:
                newVar = self[1]
                self.subs_vars.append(newVar)
                self.cursor += 2
                return self[-2] + self[-1] + self.peelWFF(vars + newVar, leading)
        else:
            self.error_message = "In parse WFF: Unknown/misplaced character: " + self[0]
            self.status = CandidateFormula.INVALID
            return ""
        return ""

    def peelSet(self, vars):
        if self.status != CandidateFormula.IN_PROGRESS:
            return ""
        self.var_map[self.cursor] = vars
        if self.remaining() == 0:
            self.error_message = "Expected: a set. Got: end of formula"
            self.status = CandidateFormula.INVALID
        elif self[0] == 'ℕ':
            self.cursor+=1
            return self[-1]
        elif self[0] in vars:
            self.cursor+=1
            return self[-1]
        elif self[0] == '𝓟':
            self.cursor+=1
            return self[-1] + self.peelSet(vars)
        elif self[0] == '∪':
            self.cursor +=1
            return self[-1] + self.peelSet(vars) + self.peelSet(vars)
        elif self[0] == '{':
            setList = SetList(self, "{", "}", ",", vars)
            return setList.str
        elif self[0] == '⟪':
            var = self[1]
            if var not in setVars:
                self.error_message = f"In comprehension: {var} is not a set variable"
                self.status = CandidateFormula.INVALID
            elif var in vars:
                self.error_message = f"In comprehension: {var} has already been used"
                self.status = CandidateFormula.INVALID
            else:
                self.cursor +=2 
                return self[-2] + self[-1] +  self.peelSet(vars) + self.peelWFF(vars + var)
        else:
            self.error_message = "In parse set: Unknown/misplaced character: " + self[0]
            self.status = CandidateFormula.INVALID
        return ""
    
    
    
    def subsSet(self, var, set):
        if var not in self.subs_vars:
            raise Exception("Not a valid substitution!")
        i = self.s.index("∀"+var)
        s2 = self.s[:i] + self.s[(i+2):]
        return CandidateFormula(s2.replace(var,set))
    
    def subsWFF(self, wffVar, wff, *setVars):
        for x in setVars:
            if x not in subVars:
                raise Exception("You have to you subVars!")
            
        lists = self.parameterized_wffs.get(wffVar)
        if lists is None:
            result = self.s.replace(wffVar, wff)
        else:                    
            subbed = []
            for phi in lists:
                wffsubbed = wff
                for x, xr in zip(setVars, phi.sets):
                    wffsubbed = wffsubbed.replace(x, xr )
                subbed.append(wffsubbed)
            result = self.s[:lists[0].start_index-1]
            for i in range(len(lists)-1):
                result += subbed[i] + self.s[(lists[i].end_index+1):(lists[i+1].start_index-1)]
            result += subbed[-1] + self.s[(lists[-1].end_index+1):]    

        c = CandidateFormula(result)
        if c.status != CandidateFormula.OK:
            raise Exception("Substitution result is not a wff! " + result)
        
        return c
        

class SetList:
    def __init__(self, cf, startChar, endChar, separator, vars):
        self.sets = []
        self.str = startChar #should be validated before
        self.start_index = cf.cursor
        cf.cursor += 1
        while cf[0] != endChar:
            nextSet = cf.peelSet(vars)
            if cf.status == CandidateFormula.INVALID:
                return
            self.str += nextSet
            self.sets.append(nextSet)
            if cf[0] == separator: 
                self.str += separator
                cf.cursor+=1
            elif cf[0] != endChar:
                cf.status=CandidateFormula.INVALID
                return
        self.str += endChar
        self.end_index = cf.cursor
        cf.cursor += 1

def testWff(s, result):
    c = CandidateFormula(s)

    computedResult = c.status == CandidateFormula.OK
    if result!=computedResult:
        message = "WRONG!!!"
    else:
        message = ''
    if c.status == CandidateFormula.OK:
        print('WFF', s, result, message, c.subs_vars)
    else:
        print('WFF', s, result, message, c.error_message)


