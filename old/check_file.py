from parse3 import CandidateFormula

import re

mp_pattern = r'mp\(\s*(\w+)\s*,\s*(\w+)\s*\)'
subsWff_pattern = r'(\w*)\.subsWff\({(.*)?(,.*)*}\)' #todo
subsSet_pattern = r'' #todo

global count
count = 0

map = {}

def next_line(file):
    while(True):
        line = file.readline()
        count += 1
        if line =='':
            return 'EOF'
        if len(line)>0:
            return line


with open("Axiom2.txt", 'r', encoding='utf-8') as file:

    while(1):
        line = next_line(file)
        if line[0] == '#':
            tags = [tag.strip() for tag in line[1:].split('#')]
            line = next_line(file)
            if line == 'Axiom':
                line = next_line
                cf = CandidateFormula(line)
                if cf.status != CandidateFormula.OK:
                    raise Exception("Axiom is not a WFF: " + line + " on line " + count)
                else:
                    for tag in tags:
                        map[tag] = cf
            else:
                m = re.match(mp_pattern, line)
                if m:

                    m.group(1)
                    m.group(2)
                else:
                    m2 = re.match(subsWFFpattern, line)


        else:
            raise Exception("Expected #, got " + line + "on line " + count)
