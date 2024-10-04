import math
while True:
    x = float(input("ph/poh: "))
    print("{:E}".format(10**(-(14-(round(-math.log(x, 10), 5))))))
