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