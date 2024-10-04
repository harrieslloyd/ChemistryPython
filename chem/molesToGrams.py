from chemFunctions import *

print("\n\n\n")
element = input("Element: ")
print('\n')
moles = float(input("Moles: "))
print('\n')
grams = molesToGrams(moles, element)
print("Grams: " + str(grams))