# Cantidad de dígitos de un número: Usa un ciclo for para recorrer 
# los caracteres de un número convertido a cadena de texto y 
# cuenta cuántos tiene.

def contar_digitos(numero):
    numero_str = str(abs(numero))
    contador = 0
    for digitos in numero_str:
        contador += 1
    return contador

numero = 123456
cantidad_digitos = contar_digitos(numero)
print(f"El numero {numero} tiene {cantidad_digitos} digitos")

