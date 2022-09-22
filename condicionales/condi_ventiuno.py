# Para determinar el promedio de tres notas y determinar si el estudiante aprobó o no

nombre = str(input("Ingrese nombre del alumno: "))
primera_nota = int(input("Ingrese primera nota: "))
segunda_nota = int(input("Ingrese segunda nota: "))
tercera_nota = int(input("Ingrese tercera nota: "))

nota_final = round((primera_nota + segunda_nota + tercera_nota) / 3)

if nota_final <= 10:
    print(nombre ,"Tu nota final es",nota_final, "estas desaprobado.")
    
else:
    print(nombre ,"Tu nota final es",nota_final, "estas aprobado.")