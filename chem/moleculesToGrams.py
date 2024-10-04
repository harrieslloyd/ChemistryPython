from chem.chemFunctions import *

print("\n\n\n")
element = input("Element: ")
print('\n')
molecules = float(input("Molecules: "))
print('\n')
grams = moleculesToGrams(molecules, element)
print("Grams: " + str(grams))