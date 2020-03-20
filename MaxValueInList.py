dizi = [1,2,3,4,5]
maxd = dizi[0]

for i in dizi[0:4]:
    if maxd<dizi[i]:
        maxd = dizi[i]

print(maxd)