from Parse6 import *

def check(s, result):
    try:
        verify(s)
        if not result:
            print(f"!!! Test Failed!! {s} should have rejected")
        else:
            print(s + " accepted, good.")
    except Exception as e:
        if result:
            print(f'!!! Test Failed!! Should have accepted {s}! {e}')
        else:
            print(s + f' rejected, correct: {e}')
        

check('𝜑', True)
check('→𝜑𝜓', True)
check('→→𝜑', False)
check('¬→𝜓𝜒', True)
check('¬𝜑→𝛾', False)
check('→→𝜑𝜓¬𝜒', True)

print(match('𝜑','→𝜒𝛾'))
print(match('→𝜒𝛾', '→→𝜑𝜓¬𝜒') )

print(match('𝜑','→𝜒𝛾¬'))