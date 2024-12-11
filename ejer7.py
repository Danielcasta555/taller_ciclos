# potencia de un número: Calcula la potencia de un número multiplicando 
# la base por sí misma tantas veces como indique el exponente, 
# utilizando un ciclo for.

def calcular_potencia(base, exponente):
    resultado = 1
    for _ in range(exponente):
        resultado *= base
    return resultado

base = 2 
exponente = 5
potencia = calcular_potencia(base, exponente)   
print(F"{base} elevado a {exponente} es {potencia}") 
