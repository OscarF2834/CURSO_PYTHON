#convertir a minutos

minutos = int(input("Por favor inserta la cantidad minutos para tranformar a horas y minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print(f"{minutos} equivale a: {horas} horas con {minutos_restantes} minutos")

#analisis de una nota
nota = float(input("Por favor inserta la nota para analizarla: "))

if(nota >= 3.0):
    print("Pasaste la materia, o la nota")
else:
    print("No pasaste la materia, vuelve a intentarlo")