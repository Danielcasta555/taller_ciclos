# Número más grande en una lista: Compara los números de una 
# lista uno por uno utilizando un ciclo for
#  para encontrar el mayor de ellos.

lista_numeros = [3, 5, 7, 10, 15]

mayor = lista_numeros[0]

for numero in lista_numeros:
    if numero > mayor:
        mayor = numero

print(f"el numero mas grande en la lista es {mayor}")