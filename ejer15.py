# Área de un triángulo: Calcula el área de un triángulo dada su base y altura 
# con la fórmula (base * altura) / 2. 
# Este ejercicio no requiere un ciclo for.

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2 
    return area

base = 10
altura = 5
area = calcular_area_triangulo(base, altura)
print(f"el area del triangulo con base {base} y altura {altura} es {area}")