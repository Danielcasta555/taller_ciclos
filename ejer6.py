# Verificación de número primo: Usa un ciclo for para verificar si un 
# número es divisible por algún número entre 2 y su raíz cuadrada. 
# Si no tiene divisores, es primo.

import math

numero = int(input("Introduce un numero entero:"))

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

if es_primo(numero):
    print(f"{numero} es un numero primo.")
else:
    print(f"{numero} no es un numero primo.")    