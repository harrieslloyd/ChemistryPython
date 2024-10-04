import math
com = ["NH4+","NO2-1","NO3-1","SO32-","SO4-2","HSO4-1","S2O3-2","C2O4-2","OH-1","PO3-3","PO4-3","HPO4-2","H2PO4-1","ClO4-1","ClO3-1","ClO2-1","ClO-1","BrO3-1","IO3-1","CH3COO-1 or C2H3O2-1","CO32-1","HCO3-1","CrO4-2","Cr2O7-2","MnO4-1","O2-2","CN-1","OCN-1","SCN-1"]
names = ["ammonium", "nitrite", "nitrate", "sulfite", "sulfate", "hydrogen sulfate", "thiosulfate", "oxalate", "hydroxide", "phosphite", "phosphate", "hydrogen phosphate", "dihydrogen phosphate", "perchlorate", "chlorate", "chlorite", "hypochlorite", "bromate", "iodate", "acetate", "acetate", "carbonate", "hydrogen carbonate (bicarbonate)", "chromate", "dichromate", "permanganate", "peroxide", "cyanide", "cyanate", "thiocyanate"]

output = "ClrHome\n"

for i in range(len(com)):
    output = output + 'Disp "' + names[i] + ": " + com[i] + "\n"
    if((i+1)%8 == 0):
        output = output + 'Wait 0.2\nPause "Next - Hit Enter\n' + 'ClrHome\n'

output = output + 'Wait 0.2\nPause "Finish - Hit Enter\n' + 'ClrHome\n'
print(output)