from chemfunc import *
from ti_system import *

print("\n\n\n")
moles = float(input("Moles: "))
print('\n')
molecules = conversion(moles, '', 'moles_to_molecules')
print("Molecules: " + str(molecules))
store_list("ANS", [molecules])
