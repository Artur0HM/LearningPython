# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

sexo = input("Cual es tu sexo: ")
grupo = input("A que grupo pertenece: ")

if sexo == 'femenino' and grupo == "a":
    nombre = input("Cual es tu nombre: ")
    print("Tu sexo es: " + sexo + " perteneces al grupo " + grupo + " tu nombre es: " + nombre )
#
#elif sexo == 'masculino' and grupo == "b":
#    nombre = input("Cual es tu nombre: ")
#    print("Tu sexo es: " + sexo + " perteneces al grupo " + grupo + " tu nombre es: " + nombre )
#    
else:
    nombre = input("Cual es tu nombre: ")
    print("Tu sexo es: " + sexo + " perteneces al grupo " + grupo + " tu nombre es: " + nombre )