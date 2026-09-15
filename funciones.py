#Las funciones son las que se tienen que utilizar para reutilizar el codigo:

def encender(estado):
    if estado == 1:
        print("El auto ya esta encendido")
    else:
        print("auto encendido")

def apagar(estado):
    if estado == 1:
        print("EL auto ya esta apagado")
    else:
        print("Auto apagado")

encender(1)
apagar(0)

suma = 90 + 67

print(f"La suma de los dos numeros es de: {suma}")

palabra = "automaticamente"
print(len(palabra))

resultado = 10**5
print(resultado)

numero_1 = 675.87
print(type(numero_1))

numero = 987654321
print(len(str(numero)))