from chemFunctions import *

print("\n\n\n")
element = input("Element: ")
print('\n')
grams = float(input("Grams: "))
print('\n')
moles = gramsToMoles(grams, element)
print("Moles: " + str(moles))