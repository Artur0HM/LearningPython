# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Ingrese su edad: "))
edad = str(edad)
ingreso = float(input("De caunto es tu ingreso mensual: "))
ingreso = str(ingreso)

if edad > '16' and ingreso > '1000':
    print("Tienes " + edad + " años, mi ingreso mensual es de: " + ingreso + " dolares, debo pagar impuestos.")

else:
    print("Tu ingreso por mes es de " + ingreso + " dolares, no pagaras impuestos." )