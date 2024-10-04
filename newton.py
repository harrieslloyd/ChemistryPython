from sympy import *
from sympy.abc import x, y, z
print("Welcome to the newton method calculator!")
func = parse_expr(input("What's the function? ").replace('^','**'))
diff = diff(func)
i = input("How many iterations of the newton method should I calculate? ")
a = float(input("What's your initial guess? "))
r = false
for l in range(int(i)):
    print((a))
    a=a-((func.evalf(subs={x:(a)}))/(diff.evalf(subs={x:a})))

print((a))