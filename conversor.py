menu = """
Bienvenido al conversor de monedas 馃槞

1 - Pesos colombianos 
2 - Pesos argentinos
3 - Pesos mexicanos
4 - soles peruanos

Elige una opci贸n: """

opcion = input(menu)

if opcion == '1':
    pesos = input("驴Cuantos pesos colombianos tienes: ")
    pesos = float(pesos)
    valor_dolar = 4428.14
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)  # round es reducieremos a dos decimales
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")

elif opcion == '2':
    pesos = input("驴Cuantos pesos argentinos tienes: ")
    pesos = float(pesos)
    valor_dolar = 140.65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)  # round es reducieremos a dos decimales
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")

elif opcion == '3':
    pesos = input("驴Cuantos pesos mexicanos tienes: ")
    pesos = float(pesos)
    valor_dolar = 20.04
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)  # round es reducieremos a dos decimales
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares")

elif opcion == '4':
    soles = input("Cuantos soles tienes: ")
    soles = float(soles)
    valor_dolar = 3.84
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str (dolares)
    print("Tienes $" + dolares + " dolares")

else:
    print("Ingresa una opci贸n correcta.")



