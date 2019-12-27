# Bir stingin istenilen bir indexini değiştirmek için replace fonksiyonu kullanlır

stirng = "Hello World"

print(stirng.replace(stirng[0:5],"HELLO"))

#Bir dizinin istenilen bir elemanını değiştirmek için ise aşağıdaki yöntem uygulanılabilir



dizi1 = [0,1,2,3,4,5,6,7] 
dizi2 = ["a","b","c","d","e","f","g"]

print(list(map(lambda x: x if x !=  dizi1[0] else dizi2[0],dizi1)))