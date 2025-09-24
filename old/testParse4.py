from parse5 import parseWff

def testWff(s, result):
    try:
        w = parseWff(s)
        if result:
            print(s + " True")
        else:
            print ("!!! TEST FAILED: " + s + " should be rejected")

        if repr(w) != s:
            print("!!! Repr failed: " + repr(w) + " != " + s)
    except Exception as e:
        if result:
            print ("!!! TEST FAILED: " + s + " should be accepted, but got " + str(e))
        else:
            print(s + " False " + str(e))

def testSubs(wffString, setString, result):
    print(f"Test set sub: {wffString}, {setString}, {result}")
    try:
        w = parseWff(wffString)
        w2 = w.setSub(setString)
        print(repr(w2))
        if not result:
            print("!!! TEST FAILED, should have rejected subsSet.")
    except Exception as e:
        print(str(e))
        if result:
            print("!!! TEST FAILED, should have succeded in subsSet")
    print()

def testMp(wffString, ant, result):
    print(f"Test mp: {wffString}, {ant}, {result}")
    try:
        w = parseWff(wffString)
        want = parseWff(ant)
        w2 = w.modusPonens(want)
        print(repr(w2))
        if not result:
            print("!!! TEST FAILED, should have rejected")
    except Exception as e:
        print(str(e))
        if result:
            print("!!! TEST FAILED, should have succeded in mp")
    print()

def testWffSub(wffString, wffVar, newWff, result):
    print(f"Test wff sub: {wffString}, {wffVar}, {newWff}, {result}")
    try:
        w = parseWff(wffString)
        w2 = parseWff(w.wffSub(wffVar, newWff))
        print(repr(w2))
        if not result:
            print("!!! TEST FAILED, should have rejected")
    except Exception as e:
        print(str(e))
        if result:
            print("!!! TEST FAILED, should have succeded in subWff")
    print()


testWffSub("→𝛼𝜓", "𝛼", "={}ℕ", True)
testWffSub("∀x∀y∀z→𝛽(x)𝛾(z,y)", "𝛾", "=XY", True)

testMp("∀x𝜑(x)", "𝜑", False)
testMp("→𝛼𝜓", "𝛼", True)


testSubs("∀x𝜑(x)", "{}", True)
testSubs("∀x𝜑(x)", "y", False)
testSubs("∀x∀y∀z→𝛽(x)𝛾(z,y)", "ℕ", True)
testSubs("∀x∀y𝜒({x,y})", "{ℕ,{}}", True)

testSubs('∀y∀z∀w=⟪xw=xy⟪xw=xz', "⟪zℕ𝛽(z)", False) 

w=parseWff("∀x∀y𝜒({x,y})").setSub("{ℕ,{}}").setSub("⟪xℕ𝛽(x)")
print(repr(w))
print()

testWff("∀x𝜑(x)", True)
testWff('𝜑𝜓', False)
testWff('',False)
testWff("∀x∀y∀z∈x∪{x,y,z}⟪wℕ𝜑", True)
testWff("∀x∀y∀z→𝛽(x)𝛾(z,y)", True)
testWff("𝛽(xz", False)
testWff("𝛽({}", False)
testWff('𝛼()', False)
testWff('∀x∀y𝜒({x,y})', True)
testWff('𝜓(x)', False)
testWff('→𝛼𝜓', True)
testWff(r'∀x∈x{}', True)
testWff('∀y∀z∀w=⟪xw=xy⟪xw=xz', True)
testWff(r'∀y∀z∀w=⟪xw=xy⟪yw=yz', False)
testWff(r'∀z∈{}𝓟z', True)
testWff('∀y=yℕ',True)
testWff('=xy', False)
testWff('∀x∀y=xy', True)
testWff('∀x∀y¬→𝜒∈xy', True)
testWff('→¬𝛼𝛼𝛼', False)
testWff('∀x→𝜑(x)∀y𝜑(x,y)', False)
testWff("→∀x𝜑(x)𝜑(x)", False)
testWff("→𝜑(x)∀x𝜑(x)", False)
testWff("∀x→𝜑(x)𝜑(x)", True)
testWff("∀→𝜑(x)𝜑(x)", False)
testWff("∀→𝜑", False)
testWff("∀x→∀x=xx=xx", False)
testWff("∀x→=xx=xx", True)