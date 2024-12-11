# Invertir un número: Recorre los dígitos de un número desde el 
# principio hasta el final utilizando un ciclo for y 
# constrúyelo en orden inverso.

def invertir_mumero(numero):
    numero_str = str(abs(numero))
    numero_invertido = ""

    for digito in numero_str[::-1]:
        numero_invertido += digito

    return int(numero_invertido)

numero = 123456
numero_invertido = invertir_mumero(numero)
print(f"El numero invertido de {numero} es {numero_invertido}")    