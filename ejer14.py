# Mínimo común múltiplo (LCM): Calcula el MCM de dos números
# utilizando el MCD previamente obtenido y 
# el producto de ambos.

def calcular_mcd(a, b):
    while b != 0:
        a, b, = b, a % b
    return a 

def calcular_mcm(a, b):
    mcd = calcular_mcd(a, b)
    mcm = abs(a * b) // mcd
    return mcm  

numero1 = 12
numero2 = 18
mcm = calcular_mcm(numero1, numero2)
print(f"el mcm de {numero1} y {numero2} es {mcm}")
   