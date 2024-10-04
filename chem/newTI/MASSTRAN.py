from ti_system import *
energy = float(input("Energy: "))
section = input("Section (Melt: m, Vaporize: v): ")

hf = 6008
hv = 40800

print("\n")

mass = 0

if section == 'v': 
    mass = (energy * 18.015)/hv

if section == 'm': 
    mass = (energy * 18.015)/hf


print('\nMass: ')


print(str(round(mass, 3)) + " g")
store_list("ANS", [mass])