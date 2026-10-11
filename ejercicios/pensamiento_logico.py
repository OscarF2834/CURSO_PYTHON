import random

#ejercicios de pensamiento logico y criticos

#un numero y decir la tabla de ese numero: 

numero_tabla = int(input("inserta el numero al cual desea hacer la tabla: "))

for i in range(11):
    print(f"{numero_tabla} * {i} = {numero_tabla*i}")
    
#contar del 1 hasta N

#pedir un numero y despues calcular la suma de todos los enteros desde 1 hasta N

N = int(input("Inserta el numero limite al cual quieres llegar: "))
suma = 0

for i in range(N + 1):
    suma += i
    print(suma)
    
print("----------------------------------")
#adivina el numero JUEGO

numero_random = random.randint(1,100)
intentos = 5

for i in range(intentos):
    
    numero_usuario = int(input("Inserta un numero del 1 al 100: "))
    
    if(numero_random == numero_usuario):
        print("Felicidades, adivinaste el numero")
    elif(numero_random < numero_usuario):
        print("el numero random es mayor")
    else:
        print("el numero random es menor")

if(numero_usuario != numero_random):
    print("Se acabaron los intentos")
    print("El numero secreto era: " , numero_random)
    
#numero primo

numero_verificar = int(input("Inserta por favor el numero que desea saber si es primo o no: "))

if(numero_verificar % 1 == 0 and numero_verificar % numero_verificar == 0):
    print("El numero es primo")
else:
    print("El numero no es primo, es compuesto")



