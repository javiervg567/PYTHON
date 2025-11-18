filas = int(input("Ingrese la cantidad de filas: "))
for i in range(1, filas +1):
    if i == 1:
        print(" " * (filas - 1) + "*")
    elif i == 2:
        print(" " * (filas - 2) + "**")
    else:
        print(" " * (filas - i) + "*" + " " * (i - 2) + "*")
for i in range(filas -1, 0, -1):
    if i == 1:
        print(" " * (filas - 1) + "*")
    elif i == 2:
        print(" " * (filas - 2) + "**")
    else:
        print(" " * (filas - i) + "*" + " " * (i - 2) + "*")    