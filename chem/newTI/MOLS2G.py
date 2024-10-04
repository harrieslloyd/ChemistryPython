from chemfunc import *
from ti_system import *

print("\n\n\n")
element = input("Element: ")
print('\n')
moles = float(input("Moles: "))
print('\n')
grams = conversion(moles, element, 'moles_to_grams')
print("Grams: " + str(grams))
store_list("ANS", [grams])