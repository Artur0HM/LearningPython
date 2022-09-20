# Iremos de vacaciones a la playa a menos que nos surja un plan mejor.

vacaciones = """
TIENES OTROS PLANES, O SI IREMOS A LA PLAYA
Escoge una opción

1 - Si tengo planes
2 - No tengo planes

Escoge una opción: """

iremos_playa = int(input(vacaciones))

if iremos_playa == 1:
    print("Entonces en la proxima iremos a la playa.")

elif iremos_playa == 2:
    print("Iremos a la palya pasare por ti.")

else:
    print("Debes escoger una opción correcta.")