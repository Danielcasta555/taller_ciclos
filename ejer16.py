# Suma de una serie geométrica: 
# Calcula la suma de los primeros n términos de una serie geométrica utilizando un ciclo for. 
# Multiplica el término inicial por la razón en cada iteración.

n = int(input("Introduce el numero de termino (n):"))
a = float(input("Introduce el termino inicial (a): "))
r = float(input("Introduce la razon (r):"))

suma_serie = 0.0

for i in range(n):
    suma_serie += a
    a *= r

print(f"La suma de los primeros {n} terminos de la serie geometrica es {suma_serie}")      