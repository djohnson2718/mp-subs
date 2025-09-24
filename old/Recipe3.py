from Parse6 import match, InsertOnlyDict
from Context3 import Context3
import copy

c = Context3()

class Recipe:
    def __init__(self, *args):
        self.hyp=args[:-1]
        self.assertion = args[-1]

    def __call__(self, f):
        #test it
        testContext = copy.deepcopy(c)
        #testContext.verbose = False
        testContext.contextName = "check-" + f.__name__ + ":"
        hypNames = ["h"+str(i) for i in range(len(self.hyp))]
        for n,w in zip(hypNames, self.hyp):
            testContext.name(testContext.axiom(w),n)      
            
        thmId = f([None] + hypNames, {}, testContext)
        if testContext[thmId].wff == self.assertion:
            print(f"Verified recipe {self.hyp} => {testContext[thmId]}")
        else:
            raise Exception(f"Recipe result doesn't match: {self.assertion} != {testContext[thmId]}.")
        
        def wrapper(hyp2, context, assertion = None):
            subs = InsertOnlyDict()
            if assertion != None:
                subs.update(match(self.assertion, assertion))
            for h,h2 in zip(self.hyp, hyp2):
                subs.update(match(h, context[h2].wff))
            return f([None]+hyp2, subs, context)
        return wrapper