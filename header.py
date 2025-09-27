from Context3 import Context3, wffVars, c



class Theorem:
    def __init__(self, nVars, name):
        self.nVars = nVars
        self.name = name
    
    def __call__(self, func):
        self.thmId = func(*wffVars[:self.nVars])
        c.name(self.thmId, self.name)
        
        def recall(*args):
            return c.subs(self.thmId, dict(zip(wffVars[:self.nVars], args)))

        return recall
    
def R_ax_mp(ph, ps, h1, h2):
    return c.mp(h1, h2)

@Theorem(2, "ax-1")
def R_ax_1(ph, ps):
    return c.axiom(f"→{ph}→{ps}{ph}")

@Theorem(3, "ax-2")
def R_ax_2(ph, ps, ch):
    return c.axiom(f"→→{ph}→{ps}{ch}→→{ph}{ps}→{ph}{ch}")

@Theorem(2, "ax-3")
def R_ax_3(ph, ps):
    return c.axiom(f"→→¬{ph}¬{ps}→{ps}{ph}")

def and_(ph, ps):
    return f"¬→{ph}¬{ps}"

@Theorem(2, "df-bi")
def R_df_bi(ph, ps):
    return c.axiom(and_(f"→↔{ph}{ps}{and_(f"→{ph}{ps}", f"→{ps}{ph}")}", f"→{and_(f"→{ph}{ps}", f"→{ps}{ph}")}↔{ph}{ps}"))

    #return c.axiom(f"→¬→↔{ph}{ps}¬→→{ph}{ps}¬→{ps}{ph}¬→¬→→{ph}{ps}¬→{ps}{ph}↔{ph}{ps}")