modal = 100000000
x = 0
z = 0

laba = [int(x), int(x), int(modal)*.1, int(modal)*.1, int(modal)*.5, int(modal)*.5, int(modal)*.5, int(modal)*.2 ]
for i in laba:
    z += 1
    print("Laba bulan ke- {0} sebesar: {1}".format(z,i))
print("Total laba adalah: {0}".format(sum(laba)))