#creando una lista con list
lista = list([21,56,78,90,True])
print(lista)

cadena = "hola"
resultado = len(cadena)
print(resultado)

#devuelve la cantidad de elementos de la lista
cantidad_elementos_lista = len(lista)
print(cantidad_elementos_lista)

#agregar elementos a la lista
agregando_con_append = lista.append(90)
print(lista)

#agregando un elemento a la lista, pasandole el indice a la cual se va a insertar
lista.insert(2,50)
print(lista)

#lo que hace extend es agregar varios elmentos a la lista
lista.extend([False,2030])
print(lista)

#eliminando un elemento de la lista por su indice
lista.pop(0)
print(lista)

#eliminando el ultimo elmento de la lista, pasando valores negativos
lista.pop(-1)
print(lista)

#removiendo un elemento de la lista por su valor
lista.remove(50)
print(lista)

#eliminando todos los elementos de la lista
#lista.clear()

#ordena de forma  ascedente, si se utiliza el parametro reverse, con true, cambia el orden 
lista.sort(reverse=True)
print(lista)

#invertir los elementos de la lista literalmente
lista.reverse()
print(lista)