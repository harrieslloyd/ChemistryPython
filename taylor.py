from sympy import *
from sympy.abc import x, y, z

function = 4*sqrt(1+x)
a=0
d1 = diff(function)
d2 = diff(d1)
d3 = diff(d2)
d4 = diff(d3)
d5 = diff(d4)

funca = function.evalf(subs={x:(a)})
d1a = d1.evalf(subs={x:(a)})
d2a = d2.evalf(subs={x:(a)})
d3a = d3.evalf(subs={x:(a)})
d4a = d4.evalf(subs={x:(a)})
d5a = d5.evalf(subs={x:(a)})



print(funca, d1a, d2a, d3a, d4a, d5a)
print(nsimplify(funca), nsimplify(d1a), nsimplify(d2a), nsimplify(d3a), nsimplify(d4a), nsimplify(d5a))
print(nsimplify(funca), nsimplify(d1a/factorial(1)), nsimplify(d2a/factorial(2)), nsimplify(d3a/factorial(3)), nsimplify(d4a/factorial(4)), nsimplify(d5a/factorial(5)))

print(nsimplify(d5a), nsimplify(d4a), nsimplify(d3a), nsimplify(d2a), nsimplify(d1a), nsimplify(funca))
print(nsimplify(d5a/factorial(5)), nsimplify(d4a/factorial(4)), nsimplify(d3a/factorial(3)), nsimplify(d2a/2), nsimplify(d1a), nsimplify(funca))


print(integrate(funca, x).evalf(subs={x:(a)}), integrate(d1a*x, x).evalf(subs={x:(a)}), integrate(d2a*x/factorial(2), x).evalf(subs={x:(a)}), integrate(d3a*x/factorial(3), x).evalf(subs={x:(a)}), integrate(d4a*x/factorial(4), x).evalf(subs={x:(a)}))