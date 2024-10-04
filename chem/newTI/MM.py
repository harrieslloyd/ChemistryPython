from ti_system import *
from chemfunc import *

com = input("Compound: ")

print("Molar mass: ")
print(molarMass(com))
store_list("ANS", [molarMass(com)])