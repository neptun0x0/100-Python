
y = 0
z = 0
x = input("Podaj Moc ")
x = float(x)
y = float(y)
z = float(z)

y = 1.35962162 * x
z = 0.73549875 * x

print(round(y))
print(str(x) + " kW = "+ str(round(y,2)) + " KM")
print(str(x) + " KM = "+ str(round(z,2)) + " kW")