# De soles a dolares

soles = input("Cuantos soles tienes: ")
soles = float(soles)
valor_dolar = 3.84
dolares = soles / valor_dolar
dolares = round(dolares, 2)
dolares = str (dolares)
print("Tienes $" + dolares + " dolares")

# De dolares a soles

dolares = input("Cuantos dolares tienes: ")
dolares = float(dolares)
valor_sol = 3.84
soles = dolares * valor_sol
soles = round(soles, 2)
soles = str (soles)
print("Tiens  S/" + soles + " soles")