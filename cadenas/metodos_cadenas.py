#metodos de cadenas
###
# se tiene como por ejemplo la funcion print, tenemos tambien la 
# funcion type, entre otras muy importantes, que se  van aa ver a continuacion
# ###

cadena1 = "Hola"
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
buscar_index = cadena1.index("o") #este si devuelve error,si no encuentra nada
print(buscar_index)

#mirar si un  dato es numerico
es_numerico = cadena1.isnumeric() ###funcion que mira si undato es numerico o no, no importa 
#si el numero esun string###
print(es_numerico)

#ahora, si es alfanumerico
es_alfanumerico = cadena1.isalpha()
print(es_alfanumerico)

#ahora,vamos a contar las concidencias que tiene un caracter
contar_concidencias = cadena1.count("s") #las vees que se repite este carater
print(contar_concidencias)

#cantidad de caracteres que tiene una cadena
contar_caracteres =  len(cadena1)
print(contar_caracteres)

#verifica si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena2.startswith("e")
print(empieza_con)

#verificasi una cendaa termina con otra cadena dad,si es asi devuelve true
termina_con =  cadena2.endswith("a")
print(termina_con)

#reemplzaa un pedazo de la cadena dada, por otra cadena dada
cadena_nueva = cadena1.replace("la","lu")
print(cadena_nueva)

#el split es para separar por el parametro dado
cadena_separada = cadena2.split("-")
print(cadena_separada)