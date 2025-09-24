import copy
from Parse6 import Context, match

c = Context()

class Recipe:
    def __init__(self, *hyp):
        self.hyp=hyp[:-1]
        self.assertion = hyp[-1]

    def __call__(self, f):
        #test it
        testContext = copy.deepcopy(c)
        #testContext.verbose = False
        hypNames = ["h"+str(i) for i in range(len(self.hyp))]
        for n,w in zip(hypNames, self.hyp):
            testContext.axiom(n,w)      
        

        def testNameFunc(i=None):
            if i==None:
                return 'test~'
            else:
                return 'test.' + str(i)
            
        f([None] + hypNames, {}, testNameFunc, testContext)
        if testContext.theorems['test'] == self.assertion:
            print(f"Verified recipe {self.hyp} => {testContext.theorems['test']}")
        else:
            raise Exception(f"Recipe result doesn't match: {self.assertion} != {testContext['test']}.")
        
        def wrapper(name, hyp2, context, assertion = None):
            def nameFunction(i=None):
                if i==None:
                    return name + '~'
                else:
                    return name + "." + str(i)
            subs = {}
            if assertion != None:
                subs.update(match(self.assertion, assertion))
            for h,h2 in zip(self.hyp, hyp2):
                subs.update(match(h, context[h2]))
            f([None]+hyp2, subs, nameFunction, context)
        return wrapper


#@Recipe('→𝜑→𝜓𝜒')
#def a2i(hyp,subs,n,c):
#    c.alias(n(1), hyp[1], subs)
#    c.wffSubs(n(2), 'frege', subs)
#    c.mp(n(), n(1), n(2))

#    a2i(n(5), n(3)) #does global context....

#a2i(name, hyp, c)