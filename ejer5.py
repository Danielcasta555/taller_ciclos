# Tabla de multiplicar de un número: Genera la tabla de multiplicar de un número dado del
#  1 al 10 utilizando un ciclo for. Por cada iteración,
#   calcula el producto y muéstralo.

numero = int(input("introduce un numero entero para generar  su tabla de multiplicar"))

for i in range(1, 11):
    producto = numero * i
    print(f"{numero} x {i} = {producto}")
