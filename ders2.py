import random #Mehmet Baki Çelik B2481.010040
z=random.randint(1,6)
p=random.randint(1,6)
if p%2==0 and z%2==0:
    print("ts kazanır")
elif p%2==1 and z%2==1:
    print("gs kazanır")
else: print("beraberlik")

import random
ts=0
gs=0
ber=0
for i in range(600000):
    z=random.randint(1,6)
    p=random.randint(1,6)
    if p%2==0 and z%2==0:
        ts=ts+1
    elif p%2==1 and z%2==1:
        gs=gs+1
    else: ber=ber+1

print('ts=%',(ts/600000)*100)
print('gs=%',(gs/600000)*100)
print('ber=%',(ber/600000)*100)




