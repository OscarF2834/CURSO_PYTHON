#solicitar notas al usuario
print("Por favor inserta a continuacion 5 notas para evaluarlas")

nota1 = float(input("Ingresa por favor la primera nota: "))
nota2 = float(input("Ingresa por favor la segunda nota: "))
nota3 = float(input("Ingresa por favor la tercera nota: "))
nota4 = float(input("Ingresa por favor la cuarta nota: "))
nota5 = float(input("Ingresa por favor la quinta nota: "))

lista_notas = [nota1, nota2, nota3, nota4, nota5]
print(f"Las notas que insertastes en la estructura de datos son: {lista_notas}")

total_notas = 0
notas_aprobadas = 0
notas_reprobadas = 0
mayor = lista_notas[0]
menor = lista_notas[0]

for i in range(len(lista_notas)):
    
    total_notas += lista_notas[i]
    
    if(lista_notas[i] >= 3.0):
        notas_aprobadas += 1
    else:
        notas_reprobadas += 1
    
    if(lista_notas[i] < mayor):
        mayor = lista_notas[i]   
    elif(lista_notas[i] > menor):
        menor = lista_notas[i]
    
promedio = total_notas / len(lista_notas)

print(f"El promedio de las notas es de: {promedio}")
print(f"La nota mas alta de la lista es de: {mayor}")
print(f"La nota mas baja de la lista es de: {menor}")
print(f"El estudiante ha aprobado una cantidad de: {notas_aprobadas} notas")
print(f"El estudiante ha reprobado una cantidad de: {notas_reprobadas} notas")