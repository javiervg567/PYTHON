"""Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.
Figura para n=6:

     *
    * *
   *   *
  * * * *
 *       *
***********"""
n = int(input("Ingrese un número entero positivo: "))
if n <= 0:
    print("Ingresa un número positivo.")
else:
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for j in range(2 * i + 1):
            if i == n - 1:
                print("*", end="")
            else:
                if (i + 1) % 2 == 0:
                    if j % 2 == 0:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    if j == 0 or j == 2 * i:
                        print("*", end="")
                    else:
                        print(" ", end="")
        print()