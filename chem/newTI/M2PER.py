valid = True
li = []
while valid: 
    mass = input("Mass: ")
    if(mass != ''):
        li.append(float(mass))
    else:
        valid = False

total = sum(li)
for i in li:
    print(str(i) + ": " + str(100 * i/total) + "%")
