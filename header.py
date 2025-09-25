from Context3 import Context3, wffVars

c = Context3()

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