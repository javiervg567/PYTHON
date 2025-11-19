"""Imprime un cuadrado de lado n con bordes de asteriscos y las dos diagonales marcadas, dejando espacios en el resto.

Figura para n=7:

*******
* *   *
*  *  *
*   * *
*  *  *
* *   *
*******"""
n = int(input("Ingrese un número entero positivo: "))
if n <= 0:
    print("Ingresa un número positivo.")
else:
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or j == 1 + min(i, n - 1 - i):
                print("*", end="")
            else:
                print(" ", end="")
        print()