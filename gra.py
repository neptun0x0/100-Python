import random



def gra(start, koniec):
    num = random.randint(start, koniec)
    rundy = int(0)
    print("Zgadnij numer pomiędzy %d a %d" %(start, koniec))
    while True:
        
        zg = input()

        try:
            i = int(zg)
            rundy = rundy + 1
            if i == num:
                print('Trafiłeś!!!')
                break
            elif i < num:
               print('Liczba jest wyższa niż ta którą podałeś')
            elif i > num:
               print('Liczba jest niższa niż ta którą podałeś')
        except ValueError:
            print("Musisz podać liczbę.")

    print("Zgadłeś w " + str(rundy) + " próbach")

gra(1, 100)