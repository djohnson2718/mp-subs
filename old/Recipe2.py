from Parse6 import match, InsertOnlyDict
from Context2 import Context2
import copy

c = Context2()

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
            testContext.axiom(w,n)      
            
        thmId = f([None] + hypNames, {}, testContext, "end check-" + f.__name__)
        if testContext[thmId] == self.assertion:
            print(f"Verified recipe {self.hyp} => {testContext[thmId]}")
        else:
            raise Exception(f"Recipe result doesn't match: {self.assertion} != {testContext[thmId]}.")
        
        def wrapper(hyp2, context, name = None, assertion = None):
            subs = InsertOnlyDict()
            if assertion != None:
                subs.update(match(self.assertion, assertion))
            for h,h2 in zip(self.hyp, hyp2):
                subs.update(match(h, context[h2]))
            return f([None]+hyp2, subs, context, name)
        return wrapper