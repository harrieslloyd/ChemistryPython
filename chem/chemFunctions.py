#Init and Needed functions
import json
import re
f = open('resources/PeriodicTable.json')
ptable = json.load(f)

avacado = 6.022 * (10**23)

def findElement(symbol):
    for element in ptable["elements"]:
        if element["symbol"] == symbol:
            return element

def elementID(compound):
    pattern = r"([A-Z][a-z]?)(\d*)|\((.*?)\)(\d*)"
    matches = re.findall(pattern, compound)

    elements = []
    counts = []

    for match in matches:
        if match[0]:
            elements.append(match[0])
            counts.append(int(match[1]) if match[1] else 1)
        elif match[2]:
            bracket_elements = re.findall(r"([A-Z][a-z]?)(\d*)", match[2])
            for bracket_match in bracket_elements:
                elements.append(bracket_match[0])
                counts.append(int(bracket_match[1]) * int(match[3]) if bracket_match[1] else int(match[3]))

    return elements, counts

def molarMass(compound):
    elements, counts = elementID(compound)

    mass = float(0)
    for i in range(len(elements)):
        mass += findElement(elements[i])["atomic_mass"] * counts[i]

    return mass



#Little Stoic

def gramsToMoles(grams, element):
    mm = molarMass(element)
    return grams/mm
def molesToGrams(moles, element):
    mm = molarMass(element)
    return moles*mm

def moleculesToMoles(molecules):
    return molecules/avacado
def molesToMolecules(moles):
    return moles*avacado

def gramsToMolecules(grams, element):
    moles = gramsToMoles(grams, element)
    return molesToMolecules(moles)
def moleculesToGrams(molecules, element):
    moles = moleculesToMoles(molecules)
    return molesToGrams(moles, element)

def conversion(starting, element, conversion_type):
    mm = molarMass(element)
    if conversion_type == 'grams_to_moles':
        return starting / mm
    elif conversion_type == 'moles_to_grams':
        return starting * mm
    elif conversion_type == 'molecules_to_moles':
        return starting / avacado
    elif conversion_type == 'moles_to_molecules':
        return starting * avacado

def valence(compound):

    elements, counts = elementID(compound)

    val = int(0)
    for i in range(len(elements)):
        if findElement(elements[i])["group"] < 2:
            val += findElement(elements[i])["group"] * counts[i]
        else:
            val += (findElement(elements[i])["group"]-10) * counts[i]
        

    return val



def solve(r, rc, rg, p, pc): 
    rm = gramsToMoles(rg, r)
    pm = (rm * pc)/rc
    pg = molesToGrams(pm, p)
    return pg
