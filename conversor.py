pesos = input("¿Cuantos pesos colombianos tienes: ")
pesos = float(pesos)
valor_dolar = 4428.14
dolares = pesos / valor_dolar
dolares = round(dolares, 2)  # round es reducieremos a dos decimales
dolares = str(dolares)
print("Tienes $" + dolares + " dólares")