
lista_ventas = [120000, 85000, 150000, 95000, 200000, 75000]

total = 0
mayor = lista_ventas[0]
menor = lista_ventas[0]
superan_100000 = 0

for i in range(len(lista_ventas)):

    # Calcular el total
    total += lista_ventas[i]

    # Encontrar la venta mayor
    if lista_ventas[i] > mayor:
        mayor = lista_ventas[i]

    # Encontrar la venta menor
    if lista_ventas[i] < menor:
        menor = lista_ventas[i]

    # Contar las ventas que superan los 100000
    if lista_ventas[i] > 100000:
        superan_100000 += 1

# Calcular el promedio
promedio = total / len(lista_ventas)

print(f"El total de ventas es: {total}")
print(f"El promedio de ventas es: {promedio}")
print(f"La venta mayor es: {mayor}")
print(f"La venta menor es: {menor}")
print(f"Las ventas que superan los 100000 son: {superan_100000}")