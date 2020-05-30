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

            print(lotto)



print("Nastęuje zolnienie blokady..... Wylosowane liczby to:  ",lotto)