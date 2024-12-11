# Cantidad de vocales en una cadena: 
# Recorre cada carácter de una cadena de texto con un ciclo for y cuenta 
# cuántos de ellos son vocales.

cadena = input("Introduce una cadena de texto")

contador_vocales = 0

vocales = "aeiouAEIOU"

for caracter in cadena:
    if caracter in vocales:
        contador_vocales += 1

print(f"La cantidad de vocales en la cadena  es: {contador_vocales}")        

