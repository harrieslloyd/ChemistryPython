from chemFunctions import *

print("\n\n\n")
element = input("Element: ")
print('\n')
grams = float(input("Grams: "))
print('\n')
molecules = gramsToMolecules(grams, element)
print("Molecules: " + str(molecules))