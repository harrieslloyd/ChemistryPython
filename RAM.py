from sympy import *
from sympy.abc import x, y, z

function = 9**x
over = [0,2]
n = 4
ramtype = 2 #0 is LRAM, 1 is MRAM, 2 is RRAM
rams = [0, 0.5, 1]

interval = Abs(over[0]-over[1])/n

sum=0

for i in range(0,n):
    print(function.evalf(subs={x:((i+rams[ramtype])*interval)}) * interval)
    sum += function.evalf(subs={x:((i+rams[ramtype])*interval)}) * interval

print(sum)