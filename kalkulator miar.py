#!/usr/bin/env python3
import math
import sys

def moc():
    y = 0
    z = 0
    x = input("Podaj Moc ")
    x = float(x)
    y = float(y)
    z = float(z)

    y = 1.35962162 * x
    z = 0.73549875 * x


    print(str(x) + " kW = "+ str(round(y,2)) + " KM")
    print(str(x) + " KM = "+ str(round(z,2)) + " kW")

def energia():
    y = 0
    z = 0
    x = input("Podaj Energię ")
    x = float(x)
    y = float(y)
    z = float(z)

    y = x / 3600000
    z = 3600000 * x

    print(str(x) + " J = "+ str(y) + " kWh")
    print(str(x) + " kWh = "+ str(round(z,2)) + " J")

def masa():
    y = 0
    z = 0
    x = input("Podaj Masę ")
    x = float(x)
    y = float(y)
    z = float(z)

    y = 0.0022046 * x
    z = 453.59237 * x

    print(str(x) + " g = "+ str(round(y,6)) + " lbs")
    print(str(x) + " lbs = "+ str(round(z,2)) + " g")

def temp():
    y = 0
    z = 0
    x = input("Podaj Temperaturę ")
    x = float(x)
    y = float(y)
    z = float(z)

    y = 273.15 + x
    z = x - 273.15


    print(str(x) + " C = "+ str(y) + " K")
    print(str(x) + " K = "+ str(round(z,2)) + " C")



print("Wciśnij 1 aby obliczyć Moc")
print("Wciśnij 2 aby obliczyć Energię")
print("Wciśnij 3 aby obliczyć Masę")
print("Wciśnij 4 aby obliczyć Temperaturę")
print("Wciśnij 5 aby wyjść ")
i = int(input())

j = 2
if i == 1:
    moc()
elif i == 2:
    energia()
elif i == 3:
    masa()
elif i == 4:
    temp()                    
elif i == 5:
    print("Bye! Bye! Bye! Bye! Bye! Bye! Bye! Bye!")
    sys.exit()
else:
    print("Nie umiesz nawet wpisać poprawnej liczby idioto?")
    print("Bye Bye!")
