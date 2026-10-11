###
# Este es un ejercicio acerca de la edicion de cursos de lenguajes de programacion
# simplemente, lo que se hace es calcular promedios y por supuesto, calcular
# las diferencias###

#esto se hace en horas
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

#Diferencias de duracion de cada uno

prom_duracion_rapido = 100 - (dalto_curso/otros_cursos_min * 100)
print(f"El curso de dalto tiene un {prom_duracion_rapido} % menos que el curso minimo de duracion")

prom_duracion_lento = 100 - (dalto_curso/otros_cursos_max * 100)
print(f"El curso de dalto tiene un {prom_duracion_lento} % menos que el curso maximo de duracion")

prom_duracion_prome = 100 - (dalto_curso/otros_cursos_prom * 100)
print(f"El curso de dalto tiene un {prom_duracion_prome} % menos que el curso promedio de duracion")