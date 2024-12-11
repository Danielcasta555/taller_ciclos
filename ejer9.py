# Máximo común divisor (MCD): Encuentra el MCD de dos números utilizando 
# el algoritmo de Euclides con un ciclo while, que repite el cálculo del residuo hasta que uno de los números sea cero.

def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a 

numero1 = 56
numero2 = 98
mcd = calcular_mcd(numero1, numero2)
print(f"el mcd de {numero1} y {numero2} es {mcd}")
