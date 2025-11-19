"""Imprime la letra M mayúscula usando asteriscos en una matriz cuadrada de tamaño impar n. Las líneas de la M deben visualizarse usando asteriscos, con espacios en el resto.

Figura para n=7:

*     *
**   **
* * * *
*  *  *
*     *
*     *
*     *
"""
n = int(input("Ingrese un número entero positivo impar: "))
if n <= 0 or n % 2 == 0:
    print("Ingresa un número positivo impar.")
else:
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if j == 0 or j == n - 1 or (j == i and j <= mid) or (j == n - 1 - i and j >= mid):
                print("*", end="")
            else:
                print(" ", end="")
        print()