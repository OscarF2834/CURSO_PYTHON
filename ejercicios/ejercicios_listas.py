#ejercicios de listas en python

#crear y consultar una lista
productos = ["Suavitel", "Jabon", "Shampoo", "Detergente", "Papel Higienico"]

#imprimiendo la lista completa
print(productos)

for producto in productos:
    print(producto)

print(f"El primer elementos de la lista es {productos[0]}")
print(f"El ultimo elementos de la lista es {productos[-1]}")
print(f"La longitud de la lista es de {len(productos)}")

#modificar los elementos de una lista
ciudades = ["Bucaramanga", "Medellin", "Bogota", "Cartagena", "Barranquilla"]
ciudades[1] = "Bucaramanga"
ciudades.append("Floridablanca")
ciudades.insert(0, "Bogota")
print(ciudades)

#crear una lista , eliminar la primera aparicion de 20, elimina el ultimo y muestra la lista

lista = [10, 20, 30, 20, 40]

lista.remove(20)
print(lista.pop())
print(lista)

#suma y promedio de una lista
numeritos = [4.0,3.5,2.8,4.7,3.0]
suma = 0

for numero in numeritos:
    suma += numero

print(suma)

#contar los aparobados de una lista

notas = [2.5, 4.0, 3.2, 1.8, 4.5, 3.0]
notas_aprobadas = 0
notas_reprobadas = 0

for noticas in notas:
    if(noticas >= 3.0):
        notas_aprobadas += 1
    else:
        notas_reprobadas += 1
print(f"El estudiante ha aprobado {notas_aprobadas} notas")
print(f"El estudiante ha reprobado {notas_reprobadas} notas")

#buscar el numero mayor de una lista

datos = [12, 45, 7, 89, 23, 56]

for i in range(len(datos)-1):
    if(datos[i] > datos[i+1]):
        mayor = datos[i]
print(f"El numero mayor de la lista es: {mayor}")

#numeros pares de una lista
numeros_totales = [1,2,3,4,5,6,7,8,9,10]
lista_pares = []

for numero in numeros_totales:
    if(numero % 2 == 0):
        lista_pares.append(numero)
print(f"La lista de numeros pares es: {lista_pares}")

lista_datos = [2,4,2,6,4,8,2]
lista_nueva = []

for numero in lista_datos:
    if(numero not in lista_nueva):
        lista_nueva.append(numero)
print(f"La lista de numeros ahora sin repetir es de: {lista_nueva}")