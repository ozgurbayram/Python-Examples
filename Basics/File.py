def sifira_kadar_carp(sayi):
    if sayi == 1: 
        return 1
    else:
        return sayi * sifira_kadar_carp(sayi-1)
 
print(sifira_kadar_carp(4))