#metodos de cadenas
###
# se tiene como por ejemplo la funcion print, tenemos tambien la 
# funcion type, entre otras muy importantes, que se  van aa ver a continuacion
# ###

cadena1 = "1aas23456789"
cadena2 = "eres muy chimba"

resultado1 = cadena1.upper()
resultado2 = cadena2.lower()
resultado3 = cadena2.capitalize()

print(resultado1)#devuelve todo lo que se puede hacer con esa cadena
print(resultado2)
print(resultado3)

#busamos una cadena en otra cadena
buscar = cadena1.find("o")#encontrar una cadena o caracter dentro de otra cadena
print(buscar)

#busqueda index o por posicion
buscar_index = cadena1.index("6") #este si devuelve error,si no encuentra nada
print(buscar_index)

#mirar si un  dato es numerico
es_numerico = cadena1.isnumeric() ###funcion que mira si undato es numerico o no, no importa 
#si el numero esun string###
print(es_numerico)

#ahora, si es alfanumerico
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)