from chemFunctions import *

def masses():
    valid = True
    li = []
    els = []
    print("Input mass. Nothing to end, '-' for the remaining")
    while valid: 
        mass = input("Mass: ")
        if mass != '':
            if mass != '-': 
                li.append(float(mass))
                els.append(input("Element: "))
            else: 
                li.append(float(input("Total Mass: "))-sum(li))
                els.append(input("Element: "))
                valid = False
        else:
            valid = False

    total = sum(li)
    percents = []
    for i in li:
        percents.append((i * 100)/total)
    return percents, els

def percents():
    valid = True
    li = []
    els = []
    print("Input percents. Nothing to end, '-' for the remaining")
    while valid: 
        per = input("Percent: ")
        if per != '':
            if per != '-': 
                li.append(float(per))
                els.append(input("Element: "))
            else: 
                li.append(100-sum(li))
                els.append(input("Element: "))
                valid = False
        else:
            valid = False
    return li, els

type = input("Starting With mass (m) or percents (p)? ")
if type == "m": li, els = masses()
elif type == "p": li, els = percents()
else: print("Invalid Input")

mm = input("Input the molar mass if you want the molecular formula: ")

moles = []
for a, b in zip(li, els): 
    moles.append(gramsToMoles(a, b))

emm = 0
for x in els: 
    emm += molarMass(x)

print("Moles: ")
print(moles)

lowest = moles[0]
for x in moles: 
    if x < lowest: lowest = x

moles = [n/lowest for n in moles]

print("Empirical Ratios: ")
print(moles)

valid = True
while valid: 
    mul = input("Multiply by: ")
    if mul != '':
        moles = [n*float(mul) for n in moles]
        print(moles)
    else:
        valid = False

if(mm != ''):
    ratio = round(float(mm)/float(emm))
    moles = [round(n)*(ratio) for n in moles]
    print("Molecular: ")
    print(moles)