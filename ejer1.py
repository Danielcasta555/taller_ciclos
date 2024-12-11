# Suma de los primeros n números naturales: 
# Calcula la suma de los números desde 1 hasta n 
# utilizando un ciclo for. Itera sobre los números en el rango de 1 a n y acumula su suma.

def suma_numeros_naturales(n):
    suma = 0
    for numero in range(1, n + 1):
        suma += numero 
    return suma
    
n = 5
resultado = suma_numeros_naturales(n)
print(f"La suma de los primeros {n} numeros naturales es: {resultado}")
