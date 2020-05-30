#!/usr/bin/env python3

print("Wpisz liczby z zakresu 1 do 49")

lista=[]
x = 0
while x < 6:
    
    z = input("Wpisz kolejna liczbe ")
    
    if int(z) > 49:
        print("Liczba jest za wysoka")          
    elif int(z) < 1:
        print("Liczba jest za niska")    
    else:      
        lista.append(z)
        print("Podane liczby to: ", lista)
        x += 1
lista = [int(i) for i in lista]

for i in range(len(lista)): #petla zew
    for j in range(len(lista)-1):
            
        if lista[j] > lista[j+1]:
            temp = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temp

            print(lista)
            