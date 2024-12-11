# Verificar si un número es palíndromo: Usa un ciclo for para 
# comparar los dígitos de un número desde los extremos hacia el centro y
#  verifica si son iguales.

numero = int(input("introduce un numero entero positivo:"))

numero_str = str(numero)
longitud = len(numero_str)
es_palindromo = True

for i in range(longitud // 2):
    if numero_str[i] != numero_str[longitud - 1 - i]:
        es_palindromo = False

if es_palindromo:
    print(f"{numero} es un numero palindromo ")
else:
    print(f"{numero} no es un numero palindromo")        