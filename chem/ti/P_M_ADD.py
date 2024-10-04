from P_FUNC import *

q, secs = findEnergy([int(input("Temp 1: ")), int(input("Temp 2: "))], float(input("Mass: ")))
phase = input("Does the additive undergo fusion (f) or vaporization (v)? ")

mass = (18.015*q)/h[phase]

print(mass)