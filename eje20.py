# Promedio ponderado: Calcula el promedio ponderado de una 
# lista de calificaciones. Multiplica cada calificación por su peso en un ciclo for y divide 
# entre el total de pesos.

calificaciones = [90, 80, 70, 85]
pesos = [0.4, 0.3, 0.2, 0.1]

suma_productos = 0
suma_pesos = 0

for i in range(len(calificaciones)):
    suma_productos += calificaciones[i] * pesos[i]
    suma_pesos += pesos[i]

promedio_ponderado = suma_productos / suma_pesos    