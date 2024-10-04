from chemFunctions import *

element = input("What is the percent of: ")
compound = input("In: ")

elMass = molarMass(element)
comMass = molarMass(compound)

print(str(round(100 * elMass/comMass, 4)) + "%")