print("----Calculadora de operaciones---- \n")


opcion = int(input("Inserta la opcion que quieres hacer: \n" \
"1. Suma \n" \
"2. Resta \n" \
"3. Multiplicacion \n" \
"4. Division \n" \
"5. Exponenciacion \n" \
"6. Modulo"))

match (opcion):
    case 1:
        numero_1 = int(input("Introduce el primer numero: "))
        numero_2 = int(input("Introduce el segundo numero: "))

        Resultado = numero_1 + numero_2
        print(f"El resultado de la suma es de: {Resultado}")

    case 2:
        numero_1 = int(input("Introduce el primer numero: "))
        numero_2 = int(input("Introduce el segundo numero: "))

        Resultado = numero_1 - numero_2
        print(f"El resultado de la resta es de: {Resultado}")

    case 3:
        numero_1 = int(input("Introduce el primer numero: "))
        numero_2 = int(input("Introduce el segundo numero: "))

        Resultado = numero_1 * numero_2
        print(f"El resultado de la multiplicacion es de: {Resultado}")

    case 4:
        numero_1 = int(input("Introduce el primer numero: "))
        numero_2 = int(input("Introduce el segundo numero: "))

        Resultado = numero_1 / numero_2
        print(f"El resultado de la division es de: {Resultado}")

    case 5:
        numero_1 = int(input("Introduce el primer numero: "))
        numero_2 = int(input("Introduce el segundo numero: "))

        Resultado = numero_1 ** numero_2
        print(f"El resultado de la potencia es de: {Resultado}")

    case 6:
        numero_1 = int(input("Introduce el primer numero: "))
        numero_2 = int(input("Introduce el segundo numero: "))

        Resultado = numero_1 % numero_2
        print(f"El resultado del modulo es de: {Resultado}")

    case _:
        print("No escogio ninguna opcion valida")