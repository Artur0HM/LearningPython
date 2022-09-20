# Programa que simula el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritméticas básicas (suma, resta, multiplicación y división) con valores numéricos enteros. El usuario debe especificar la operación con el primer carácter del primer parámetro de la línea de comandos.


calculadora = """
OPERACIONES ARITMETICAS

1 - SUMA
2 - RESTA
3 - MULTIPLICACIÓN
4 - DIVISIÓN

Elegi una opción: """

operaciones     = int(input(calculadora))
primer_numero   = int(input("Ingrese el primer número: "))
segundo_numero  = int(input("Ingrese el segundo número: "))

suma            = primer_numero + segundo_numero
resta           = primer_numero - segundo_numero
multiplicacion  = primer_numero * segundo_numero
division        = primer_numero / segundo_numero

if operaciones == 1:
    print("La suma de", primer_numero , "+" , segundo_numero , "=" , suma)

elif operaciones == 2:
    print("La resta de", primer_numero , "-" , segundo_numero , "=" , resta)

elif operaciones == 3:
    print("La multiplicación de", primer_numero , "x" , segundo_numero , "=" , multiplicacion)

elif operaciones == 4:
    print("La división de", primer_numero , "/" , segundo_numero , "=" , division)
    
else:
    print("Debes elegir una opción correcta.")
    # corregir el bug 