from chemfunc import *
from ti_system import *

element = input("What is the percent of: ")
compound = input("In: ")

elMass = molarMass(element)
comMass = molarMass(compound)

print(str(round(100 * elMass/comMass, 4)) + "%")
store_list("ANS", [100 * elMass/comMass])