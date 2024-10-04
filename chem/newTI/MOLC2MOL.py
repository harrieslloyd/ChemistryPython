from chemfunc import *
from ti_system import *

print("\n\n\n")
molecules = float(input("Molecules: "))
print('\n')
moles = conversion(molecules, '', 'molecules_to_moles')
print("Moles: " + str(moles))
store_list("ANS", [moles])