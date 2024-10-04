from chemfunc import *

compound = input("Empirical: ")
mm = float(input("Molar Mass: "))

els, counts = elementID(compound)

emm = molarMass(compound)

r = mm/emm

counts = [round(n)*round(r) for n in counts]

print(counts)
store_list("ANS", [counts])
