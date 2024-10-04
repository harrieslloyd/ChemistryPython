from chemFunctions import *

print("\n\n\n")
r = str(input("r: "))
rc = int(input("rc: "))
rg = float(input("rg: "))
p = str(input("p: "))
pc = int(input("pc: "))
print("\n")

result = solve(r, rc, rg, p, pc)
print("Result: " + str(result))