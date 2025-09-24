from parse3 import *

a = CandidateFormula("∀x𝜑(x)").subsSet("x", "ℕ")
print(a)

a = CandidateFormula("→∀x𝜑(x)∀y𝜓(y)").subsSet("y","ℕ")
print(a)

d = CandidateFormula("→𝜑(ℕ,{})𝜒").subsWFF("𝜑","∈XY","X","Y")
print(d)

e=CandidateFormula("∀x𝜑(x,ℕ)").subsWFF("𝜑","∈XY","X","Y")
print(e)

f=CandidateFormula("∀x∀y𝜑(y,x)").subsWFF("𝜑","∈XY","X","Y")
print(f)

f=CandidateFormula("∀x∀y→𝜑(y,x)𝜑({},𝓟y)").subsWFF("𝜑","∈XY","X","Y")
print(f)

f=CandidateFormula("→𝜑→𝜓𝜑").subsWFF("𝜓", "𝜑")
print(f)

#should be error
#f=CandidateFormula("∀x∀y→𝜑(y,x)𝜑({},𝓟y)").subsWFF("𝜑","∈X","X","Y")
#print(f)

testWff('∀x→𝜑(x)∀y𝜑(x,y)', False)
testWff('',False)
testWff("∀x∀y∀z∈x∪{x,y,z}⟪wℕ𝜑", True)
testWff("∀x𝜑(x)", True)
testWff("∀x∀y∀z→𝛽(x)𝛾(z,y)", True)
testWff("𝛽(xz", False)
testWff('𝛼()', True)
testWff('∀x∀y𝜒({x,y})', True)
testWff('𝜓(x)', False)
testWff('→𝛼𝜓', True)
testWff(r'∀x∈x{}', True)
testWff(r'∀y∀z∀w=⟪xw=xy⟪xw=xz', True)
testWff(r'∀y∀z∀w=⟪xw=xy⟪yw=yz', False)
testWff(r'∀z∈{}𝓟z', True)
testWff('∀y=yℕ',True)
testWff('𝜑𝜓', False)
testWff('=xy', False)
testWff('∀x∀y=xy', True)
testWff('∀x∀y¬→𝜒∈xy', True)
testWff('→¬𝛼𝛼𝛼', False)