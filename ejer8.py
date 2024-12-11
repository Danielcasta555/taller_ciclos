# Media de una lista de números: Recorre cada elemento de una lista con un ciclo for, 
# acumula su suma y divide entre el número total de elementos para calcular la media.

lista_numeros = [3, 5, 7, 10, 15]

suma = 0

for numero in lista_numeros:
    suma += numero 

media = suma / len(lista_numeros)

print(f"La media de lista es: {media}")