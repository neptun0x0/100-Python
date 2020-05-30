#!/usr/bin/env python3

 print("Wpisz liczby z zakresu 1 do 49")

lista=[]
for x in range(6):
    x+=1
    print("Wpisz kolejna liczbe")
    lista.append(input(lista))
    

print("Podane liczby to: ", lista)

for i in range(len(lista)): #petla zew
    for j in range(len(lista)-1):
            
        if lista[j] > lista[j+1]:
            temp = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temp

            print(lista)
            