# Suma de los dígitos de un número con ciclos: Extrae cada dígito de un 
# número utilizando operaciones matemáticas y acumula su suma dentro de
#  un ciclo.

numero = int(input("Introduce un numero entero positivo:"))

suma_digito = 0

while numero > 0:
    digito = numero % 10 
    suma_digito += digito
    numero = numero // 10

    print(f"La suma de los digitos es: {suma_digito}")