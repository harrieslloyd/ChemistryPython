from chemfunc import *
from ti_system import *

print("\n\n\n")
element = input("Element: ")
print('\n')
grams = float(input("Grams: "))
print('\n')
moles = conversion(grams, element, 'grams_to_moles')
print("Moles: " + str(moles))

store_list("ANS", [moles])
