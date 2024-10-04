from chemFunctions import *

print("\n\n\n")
r = str(input("reactant: "))
rc = int(input("reactant count: "))
rg = float(input("reactant grams: "))
p = str(input("product: "))
pc = int(input("product count: "))
print("\n")

result = solve(r, rc, rg, p, pc)
print("Product Grams: " + str(result))