# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numero_uno = float(input("Ingrese el primer número: "))
numero_dos = float(input("Ingrese el segundo número: "))

resultado = numero_uno / numero_dos

if numero_dos == 0:
    print("El divisor es 0 ERROR")
else:
    print(numero_uno/numero_dos) 
