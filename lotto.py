import random
#!/usr/bin/env python3


print("Wpisz liczby z zakresu 1 do 49")

lista=[]
x = 0
y = 0
zl = 0
while len(lista) < 6:   #coś mi rekurencja z x nie działała
    
    z = input("Wpisz kolejna liczbe ")
    
    if int(z) > 49:
        print("Liczba jest za wysoka ")          
    elif int(z) < 1:
        print("Liczba jest za niska ")    
    else:      
        lista.append(z)
        for i in range(len(lista)-1):
            if lista[i] == z:
                lista.pop()
                print("Podałeś tą samą liczbę 2 raz ")
            
        print("Podane liczby to: ", lista)
lista = [int(i) for i in lista]
print("Podane liczby to: ", lista)


for i in range(len(lista)): #sortowanie
    for j in range(len(lista)-1):
            
        if lista[j] > lista[j+1]:
            temp = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temp

print("Podane liczby to: ", lista)
            
            

import random
lotto = []
zl = 0


while len(lotto) < 6:   
    
    zl = random.randint(1, 49)
    
         
    lotto.append(zl)
    for i in range(len(lotto)-1):
            if lotto[i] == zl:
                lotto.pop()
                
            

    

for i in range(len(lotto)): #sortowanie
    for j in range(len(lotto)-1):
            
        if lotto[j] > lotto[j+1]:
            temp = lotto[j]
            lotto[j] = lotto[j+1]
            lotto[j+1] = temp

      



print("Nastęuje zolnienie blokady..... Wylosowane liczby to:  ",lotto)
zz = 0
wynik = []

for i in range(len(lista)-1): #sortowanie
    zz = lista[i]
    if zz in lotto:
        wynik.append(zz)  
wynik2 = []


print("Trafiłeś",len(wynik))
print("Te liczby to ", wynik)
            
