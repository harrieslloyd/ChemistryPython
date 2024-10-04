def mcat(m, c, t):
    return m*c*t

h = {"f": 6008, "f": 40800}
s = {"i": 2.09, "w": 4.184, "v": 1.87}

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

def findEnergy(io, m):

    i = sorted(io)

    secs = sections(i[0], i[1])

    energy = 0

    for p in secs:
        if p==0:
            dt = min(i[1], 0)-i[0]
            e = mcat(m, s["i"], dt)
            energy += e

        if p==1:
            e = h["f"] * (m/18.015)
            energy += e

        if p==2:
            dt = min(i[1], 100)-max(0, i[0])
            e = mcat(m, s["w"], dt)
            energy += e

        if p==3: 
            e = h["v"] * (m/18.015)
            energy += e

        if p==4: 
            dt = i[1]-max(100, i[0])
            e = mcat(m, s["v"], dt)
            energy += e


    if(io[0] > io[1]):
        energy = energy * -1
    return energy, secs