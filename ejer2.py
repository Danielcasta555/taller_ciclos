# Factorial de un número dado: 
# Encuentra el factorial de un número multiplicando
#  todos los números desde 1 hasta ese número con un ciclo for. 
#  Asegúrate de inicializar la variable acumuladora en 1.

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = 5 
resultado = factorial(n)
print(f"el factorial de {n} es: {resultado}")