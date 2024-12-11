# Suma de los dígitos de un número: 
# Recorre cada dígito de un número 
# (convirtiéndolo en una cadena de texto) 
# y suma sus valores utilizando un ciclo for.

def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

numero = 12225
resultado = suma_digitos(numero)
print(f"la suma de los digitos de {numero} es {resultado}")    
