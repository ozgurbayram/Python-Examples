# lamda fonksiyonları fonksiyon oluşturmak için basit bir yöntemdir def ile aynı görevi yapar

# def() ile yazılan fonksiyon
def topla1(x,y,z):
    return x+y+z

print(topla1(1,3,5))

# lamda ile yazılan fonksiyon

topla = lambda x,y,z: x+y+z

print(topla(1,3,5))