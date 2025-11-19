"""Imprime una estrella de ocho puntas combinando líneas verticales, horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n"""
n = int(input("Ingresa un número impar positivo: "))
if n <= 0 or n % 2 == 0:
    print("Ingresa un número positivo impar.")
else:
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if i == mid or j == mid or i == j or i + j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
        