# Búsqueda binaria: Divide una lista ordenada en mitades para
#  encontrar un elemento específico utilizando un ciclo while. 
#  Este ejercicio utiliza índices y comparación.

def busqueda_binaria(lista, objetivo):

    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2

        if lista[medio] == objetivo:
            return medio
        
        elif lista[medio] < objetivo:
            inicio = medio + 1 

        else:
            fin = medio - 1

    return 1

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19 ]
objetivo = 7 

resultado = busqueda_binaria(lista, objetivo)
if resultado != 1:
    print(f"Elemento encontrado en el indice {resultado}")
else:
    print("elemento no encontrado")    


