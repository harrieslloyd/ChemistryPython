from chemFunctions import *


r1 = input("reactant 1: ")
r1count = int(input("amount: "))
r1grams = float(input("grams: "))
r2 = input("reactant 2: ")
r2count = int(input("amount: "))
r2grams = float(input("grams: "))
p = input("product: ")
pcount = int(input("amount: "))

p1 = solve(r1, r1count, r1grams, p, pcount)
p2 = solve(r2, r2count, r2grams, p, pcount)
print(p1)
print(p2)
if p1 > p2:
    print("Limiting Reactant is: " + r2)
    print("Grams of product produced: " + str(p2))
    otherused = solve(r2, r2count, r2grams, r1, r1count)
    otherleftover = r1grams - otherused
    print("Other Leftover: " + str(otherleftover))
else: 
    print("Limiting Reactant is: " + r1)
    print("Grams of product produced: " + str(p1))
    otherused = solve(r1, r1count, r1grams, r2, r2count)
    otherleftover = r2grams - otherused
    print("Other Leftover: " + str(otherleftover))