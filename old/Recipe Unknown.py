from parse5 import parseWff

class Recipe:
    def __init__(self,*hyp):
        self.wffHyp = [parseWff(w) for w in hyp]

    def getSubs(self, *hypNames):
        subs = {}
        for h1, h2 in zip(self.wffHyp, hypNames):
            subs.update(getSubs(h1, map[h2]))
        return subs

    def check(self):
        c = globalContext.clone()

        hypNames = ["h"+i for i in range(len(self.wffHyp))]

        for n,w in zip(hypNames, self.wffHyps):
            c.put(n, w)
        
        self('test', *hypnames, c)

class mp2(Recipe):
    def __init__(self):
        super('𝜑','𝜓','→𝜑→𝜓𝜒')

    def __call__(name, *hypNames):
        name += '.mp2'
        modusPonens(name + '.4', hypNames[2], hypNames[0])
        modusPonens(name, name + '.4', hypNames[1])

class mp2b(Recipe):
    def __init__(self):
        super('𝜑','→𝜑𝜓','→𝜓𝜒')

    def __call__(*hypNames):
        name += '.mp2b'
        modusPonens(name + '.3', hypNames[1], hypNames[0])
        modusPonens(name, hypNames[2], name + '.3')

class ali(Recipe): #special because it needs to introduce  something not determinable from the hypthosis.
    def __init__(self):
        super('𝜑')

    def __call__(name, intro, orig):
        name += '.ali'
        wffSubs(name + '.2', 'simp', {'𝜓':intro, '𝜑':orig})
        modusPonens(name, name + '.2', orig)

class _2ali(Recipe):
    def __init__(self):
        super('𝜑')

    def __call__(name, intro1, intro2, orig):
        name += '.2ali'
        ali(name + '.1', orig, intro1)
        ali(name, name + '.1', intro2)

class a2i(Recipe):
    def __init__(self):
        super('→𝜑→𝜓𝜒')

    def __call__(self, name, hyp):
        name += '.a2i'
        subs = self.getSubs(hyp)
        wffSubs(name + '.2', 'frege', subs)
        modusPonens(name, name + '.2', hyp)




def getSubs(origHyps, names):
    return subs
        
def f(name, *hypNames):
    subs = getSubs(['my hard coded hyps'], hypNames)
    #Before using any thing that is not a hyp, do the subs on it.
    modusPonens(name = name + ".4", target = name + '.1')

