#Init and Needed functions
import json
import re
f = open('resources/PeriodicTable.json')
ptable = json.load(f)

output = ''

for i in range(100):
    output += 'If Str2="' + ptable["elements"][i]["symbol"].upper() + '":M+(' + str(ptable["elements"][i]["atomic_mass"]) + "*C)→M\n"

print(output)