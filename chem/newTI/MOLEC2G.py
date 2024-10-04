from chemfunc import *
from ti_system import *

print("\n\n\n")
element = input("Element: ")
print('\n')
molecules = float(input("Molecules: "))
print('\n')
moles = conversion(molecules, element, 'molecules_to_moles')
grams = conversion(moles, element, 'moles_to_grams')
print("Grams: " + str(grams))
store_list("ANS", [grams])