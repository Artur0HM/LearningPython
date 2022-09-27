# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('!Estoy aprendiendo a usar funciones¡')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


# def conversacion (mensaje):
#     print('Hola')
#     print('Cómo estás')
#     print(mensaje)
#     print('Adios')

# opcion = int(input('Elige una opción (1 - 2 - 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opción 1')

# elif opcion == 2:
#     conversacion('Elegiste la opción 2')

# elif opcion == 3:
#     conversacion('Elegiste la opción 3')

# else:
#     print('Escribe la opción correcta')
    


# def suma (a, b):
#     print('Se suman dos números')
#     resultado = a + b
#     return resultado

# sumatoria = suma (1,4)
# print(sumatoria)

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos" + tipo_pesos + " tienes: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)  # round es reducieremos a dos decimales
    dolares = str(dolares)
    print("Tienes $", dolares , " dólares")

menu = """
Bienvenido al conversor de monedas 😙

1 - Pesos colombianos 
2 - Pesos argentinos
3 - Pesos mexicanos
4 - soles peruanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("pesos colombianos", 4428.14)

elif opcion == 2:
    conversor("pesos argentinos", 140.65)

elif opcion == 3:
    conversor("pesos mexicanos", 20.04)

elif opcion == 4:
    conversor("soles", 3.84)

else:
    print("Ingresa una opción correcta.")

