print("Note: This only works for problems with no phase changes. ")
m = float(input("Mass of additive: "))
t1 = float(input("Higher Temp: "))
t2 = float(input("Lower Temp: "))
dt = t1-t2

print(6008*(m/18.015)/(4.184*dt))

