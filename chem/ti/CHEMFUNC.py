from ti_system import *

masses = recall_list("MASS")
elementlist = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm']
avacado = 6.022 * (10**23)

# Rest of the code remains the same
def findElement(symbol):
    for element in elementlist:
        if element == symbol:
            return masses[elementlist.index(element)]

def elementID(compound):
    elements = []
    counts = []

    i = 0
    while i < len(compound):
        char = compound[i]

        if char.isupper():
            element = char
            i += 1
            while i < len(compound) and compound[i].islower():
                element += compound[i]
                i += 1

            count = ""
            while i < len(compound) and compound[i].isdigit():
                count += compound[i]
                i += 1
            counts.append(int(count) if count else 1)
            elements.append(element)

        elif char == '(':
            i += 1
            inner_elements, inner_counts, i = extract_elements(compound, i)

            count = ""
            while i < len(compound) and compound[i].isdigit():
                count += compound[i]
                i += 1
            multiplier = int(count) if count else 1

            for e, c in zip(inner_elements, inner_counts):
                elements.append(e)
                counts.append(c * multiplier)

        else:
            i += 1

    return elements, counts

def extract_elements(compound, i):
    elements = []
    counts = []

    while i < len(compound) and compound[i] != ')':
        sub_element = compound[i]
        i += 1
        while i < len(compound) and compound[i].isalpha():
            sub_element += compound[i]
            i += 1

        count = ""
        while i < len(compound) and compound[i].isdigit():
            count += compound[i]
            i += 1

        counts.append(int(count) if count else 1)
        elements.append(sub_element)

    i += 1  # Move past the closing bracket
    return elements, counts, i

def molarMass(compound):
    elements, counts = elementID(compound)

    mass = float(0)
    for i in range(len(elements)):
        mass += findElement(elements[i]) * counts[i]

    return mass

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

def solve(r, rc, rg, p, pc):
    rm = conversion(rg, r, 'grams_to_moles')
    pm = (rm * pc) / rc
    pg = conversion(pm, p, 'moles_to_grams')
    return pg
