from chemfunc import *
from ti_system import *

print("\n\n\n")
element = input("Element: ")
print('\n')
grams = float(input("Grams: "))
print('\n')
moles = conversion(grams, element, 'grams_to_moles')
molecules = conversion(moles, element, 'moles_to_molecules')
print("Molecules: " + str(molecules))
store_list("ANS", [molecules])