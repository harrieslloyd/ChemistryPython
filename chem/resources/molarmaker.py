import json
f = open('chem/resources/PeriodicTable.json')
ptable = json.load(f)

els = []
mm = []
for i in range(100):
    els.append(ptable["elements"][i]["symbol"])
    mm.append(ptable["elements"][i]["atomic_mass"])


print(els)
print(mm)