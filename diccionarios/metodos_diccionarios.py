diccionario = {
    "nombre" : 'oscar',
    "apellido" : 'Alvarado',
    "subs" : 1000
}

claves = diccionario.keys()
print(claves)

#Se obetiene un elemento con get 
valor_de_jajsjs = diccionario.get("jsjsjjsj")

#eliminando un elemento del diccionario
valor_eliminado = diccionario.pop("subs")

#obteniendo un diccionario iterable, osea que se puede recorrer. dicc_items
dicc_items = diccionario.items()

#eliminando todos los elementos del diccionario
#diccionario.clear()

print(dicc_items)