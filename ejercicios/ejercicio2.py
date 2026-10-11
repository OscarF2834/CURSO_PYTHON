#generar una calculadora de dos numeros de forma que los numeros los inserte el usuario

numero1 = float(input("Inserta por favor el primer numero: "))
numero2 = float(input("Inserta por favor el segundo numero: ")) 

resultado = numero1 + numero2

print(f"El resultado de {numero1} + {numero2} es igual a {resultado}")

#vamos hacer ahora una minicalculadora

numero1 = int(input("Inserta por favor el primer numero: "))
numero2 = int(input("Inserta por favor el segundo numero: ")) 

opcion = int(input("Inserte la opcion, si es 1 es suma, si es 2 es resta, 3 multiplicacion y 4 division"))

match opcion:
    case 1:
        resultado = numero1 + numero2
        print(f"El resultado de la operacion es de: {resultado}")
    case 2:
        resultado = numero1 - numero2
        print(f"El resultado de la operacion es de: {resultado}")
    case 3:
        resultado = numero1 * numero2
        print(f"El resultado de la operacion es de: {resultado}")
    case 4:
        resultado = numero1 / numero2
        print(f"El resultado de la operacion es de: {resultado}")
    case _:
        print("No insertastes ninguna operacion valida")
        
#numero impar o par
numero = int(input("Por favor inserta un numero entero: "))

if(numero % 2 == 0):
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} no es par")
    
#El numero mayor de dos numeros

numero_uno = int(input("Inserta por favor el primer numero: "))
numero_dos = int(input("Inserta por favor el segundo numero: "))

if(numero_uno > numero_dos):
    print(f"El numero {numero_uno} es mayor que el numero {numero_dos}")
elif(numero_uno < numero_dos):
    print(f"El numero {numero_uno} es menos que el numero {numero_dos}")
else:
    print("Los dos numeros son iguales")
    
#clasificar las edades y decir si es mayor de edad o las clasificaciones que se piden

edad = float(input("Por favor indica la edad que tienes: "))

if(edad < 13):
    print("Tu eres un niño recien")
elif(edad >= 13 and edad<18):
    print("Tu eres un adolescente, o un muchacho muy joven")
elif(edad >= 18 and edad<60):
    print("Tu lo que eres es un adulto relativamente joven")
else:
    print("Tu ya eres un adulto mayor")