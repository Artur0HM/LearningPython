# En caso de que prefieran vino y no agua, el menú es más costoso.

elegir = """

Que bebida vas a elegir

1 - VINO
2 - AGUA

Escoge una opción: """

vino_agua = int(input(elegir))

if vino_agua == 1:
    print("Escogiste vino el costo del menu sera más alto.")

elif vino_agua == 2:
    print("Escogiste agua el costo del menu sera normal.")

else:
    print("Debes elegir una opción correcta.")


