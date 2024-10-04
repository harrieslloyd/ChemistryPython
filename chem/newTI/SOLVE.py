from chemfunc import *
from ti_system import *

print("\n\n\n")
r = str(input("Reactant: "))
rc = int(input("Reactant Count: "))
rg = float(input("Reactant mass: "))
p = str(input("Product: "))
pc = int(input("Product Count: "))
print("\n")

result = solve(r, rc, rg, p, pc)
print("Result: " + str(result))
store_list("ANS", [result])