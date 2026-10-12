lista_numeros = [3,8,12,5,7,10,15,20]
numeros_pares = []

for i in range(len(lista_numeros)):
    if(lista_numeros[i] % 2 == 0):
        numeros_pares.append(lista_numeros[i])

print(f"Los numeros pares de la lista son: {numeros_pares}")

print("--------------------------------")

notas = [2.5,4.0,3.2,1.8,4.5,3.0]

lista_aprobadas = []

for nota in notas:
    if(nota >= 3.0):
        lista_aprobadas.append(nota)
print(f"La lista de notas aprobadas son: {lista_aprobadas}")

print("---------------------------------")

#Contar los mayores de edad
lista_edades = [15,22,17,30,16,45,18]
mayores_edad = 0

for edad in lista_edades:
    if(edad >= 18):
        mayores_edad += 1
print(f"La cantidad de mayores de edad que ahy en la lista es de: {mayores_edad}")

print("-------------------------------------------")

#contar el total de las ventas superiores a 50000

precios = [45000, 120000, 80000, 200000, 35000]
total_ventas_superiores = 0

for precio in precios:
    if(precio >= 50000):
        total_ventas_superiores += precio
print(f"El valor total de las ventas superior a 50000 es de: {total_ventas_superiores}")

print("-------------------------------------------")

#Encontrar el numero menor de la lista

numeros = [34,12,56,7,23,9]
numero_menor = numeros[0]

for i in range(len(numeros)):
    if(numeros[i]<numero_menor):
        numero_menor = numeros[i]
print(f"El numero menor de la lista es {numero_menor}")

#transformar una lista

lista_valores = [2,4,6,8,10]
nueva_lista = []

for valor in lista_valores:
    potencia = valor * valor
    nueva_lista.append(potencia)
print(f"La nueva lista de valores es {nueva_lista}")

#buscar un producto de una lista

productos = ["renault 9", "bmw", "audi", "mustang gt350"]
producto_encontrar = input("Inserte por favor el producto que quiere buscar: ")
encontrado = False

for producto in productos:
    if(producto_encontrar == producto):
        encontrado = True
print(f"El producto ha sido encontrado?: {encontrado}")