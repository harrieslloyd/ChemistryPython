def mcat(m, c, t):
    return m*c*t

def sectioncheck(s, t):
    if s == 0: 
        return t < 0
    if s == 1: 
        return t == 0
    if s == 2: 
        return t > 0 and t < 100
    if s == 3: 
        return t == 100
    if s == 4: 
        return t > 100

def sections(t1, t2):
    allsecs = []
    for i in range(t1, t2+1):
        for x in range(0,5):
            if(sectioncheck(x, i)):
                allsecs.append(x)
    secs = []
    for k in allsecs:
        if k not in secs: 
            secs.append(k)
    return secs

io = [int(input("Temp 1: ")), int(input("Temp 2: "))]
i = sorted(io)
m = float(input("Mass: "))

secs = sections(i[0], i[1])

energy = 0

si = 2.09
sw = 4.184
sv = 1.87

hf = 6008
hv = 40800

print("Goes through sections:" , secs)


for p in secs:
    if p==0:
        dt = min(i[1], 0)-i[0]
        e = mcat(m, si, dt)
        print("Ice: " + str(round(e, 3)))
        energy += e

    if p==1:
        e = hf * (m/18.015)
        print("Melting: " + str(round(e, 3)))
        energy += e

    if p==2:
        dt = min(i[1], 100)-max(0, i[0])
        e = mcat(m, sw, dt)
        print("Water: " + str(round(e, 3)))
        energy += e

    if p==3: 
        e = hv * (m/18.015)
        print("Boiling: " + str(round(e, 3)))
        energy += e

    if p==4: 
        dt = i[1]-max(100, i[0])
        e = mcat(m, sv, dt)
        print("Vapor: " + str(round(e, 3)))
        energy += e

print('Energy: ')

if(io[0] > io[1]):
    energy = energy * -1

print(str(round(energy, 3)) + " J")