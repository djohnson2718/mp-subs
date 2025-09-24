from Recipe3 import Recipe, c
from Parse6 import subsFromDict, match

c.name(c.axiom('→𝜑→𝜓𝜑'), 'ax-1')
c.name(c.axiom('→→𝜑→𝜓𝜒→→𝜑𝜓→𝜑𝜒'), 'ax-2')

@Recipe('𝜑','𝜓','→𝜑→𝜓𝜒', '𝜒')
def mp2(hyp, subs, c):
    s1 = hyp[2]
    s2 = hyp[1]
    s3 = hyp[3]
    s4 = c.mp(s2, s3)
    return c.mp(s1,s4)

@Recipe('𝜑', '→𝜓𝜑')
def ali(hyp, subs, c):
    s1 = hyp[1]
    s2 = c.subs('ax-1', subs)
    return c.mp(s1,s2)

@Recipe('𝜑','→𝜓→𝜒𝜑')
def _2ali(hyp, subs, c):
    s1 = hyp[1]
    s2 = ali([s1], c, assertion=subsFromDict('→𝜒𝜑', subs))
    return ali([s2], c)

@Recipe('→𝜑→𝜓𝜒','→→𝜑𝜓→𝜑𝜒')
def a2i(hyp, subs, c):
    s1 = hyp[1]
    s2 = c.subs('ax-2', subs)
    return c.mp(s1,s2)

@Recipe('→𝜑𝜓','→𝜑→𝜓𝜒', '→𝜑𝜒')
def mpd(hyp, subs, c):
    s1 = hyp[1]
    s2 = hyp[2]
    s3 = a2i([s2], c) #suspect
    return c.mp(s1, s3)

s1 = c.subs('ax-1', {'𝜓':'𝜑'})
s2 = c.subs('ax-1', {'𝜓':'→𝜑𝜑'})
c.name(mpd([s1,s2], c), 'id')

s1 = c.subs('id', {}, firstMatch='→𝜓𝜓')
c.name(ali([s1], c, assertion='→𝜑→𝜓𝜓'), 'idd')

@Recipe('→𝜑𝜓','→𝜓𝜒', '→𝜑𝜒')
def syl(hyp, subs, c):
    s1 = hyp[1]
    s2 = hyp[2]
    s3 = ali([s2], c, assertion=subsFromDict('→𝜑→𝜓𝜒', subs))
    return mpd([s1,s3], c)

@Recipe('→𝜑𝜓', '→𝜑→𝜒𝜓')
def ald(hyp, subs, c):
    s1 = hyp[1]
    s2 = c.subs('ax-1', subs, '→𝜓→𝜒𝜓')
    return syl([s1,s2], c) #suspect 

@Recipe('→𝜑𝜓','→𝜑→𝜒→𝜃𝜓')
def _2ald(hyp, subs, c):
    s1 = hyp[1]
    s2 = ald([s1], c, subsFromDict('→𝜑→𝜃𝜓', subs))
    return ald([s2], c, subsFromDict('→𝜑→𝜒→𝜃𝜓', subs))

c.name(_2ald(['id'],c),'2ali')

@Recipe('→𝜑→𝜓𝜒','→𝜓→𝜒𝜃', '→𝜑→𝜓𝜃')
def sylcom(hyp, subs, c):
    s1 = hyp[1]
    s2 = hyp[2]
    s3 = a2i([s2],c) #suspect
    return syl([s1,s3], c) #suspect

@Recipe('→𝜑𝜓','→𝜒→𝜓𝜃', '→𝜑→𝜒𝜃')
def syl5com(hyp, subs, c):
    s1 = hyp[1]
    s2 = ald([s1], c, assertion=subsFromDict('→𝜑→𝜒𝜓',subs))
    s3 = hyp[2]
    return sylcom([s2,s3],c) #suspect

@Recipe('→𝜑→𝜓𝜒', '→𝜓→𝜑𝜒')
def com12(hyp, subs, c):
    s1 = c.subs('id', subs, '→𝜓𝜓')
    s2 = hyp[1]
    return syl5com([s1,s2],c) #suspect

s1 = c.subs('id', match(c['id'].wff, '→→𝜑𝜓→𝜑𝜓'))
c.name(com12([s1],c),'pl2.27')

c.makePage("theorems.html")