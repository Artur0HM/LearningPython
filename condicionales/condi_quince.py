# Como no ordenes tu habitación no te daré un chocolate.

habitacion = """
ARREGLASTE TU HABITACIÓN 

1 - SI
2 - NO

Escoge una opción: """

ordenaste = int(input(habitacion))

if ordenaste == 1:
    print("Por arreglar tu habitación te voy a dar Chocolate.")

elif ordenaste == 2:
    print("Por no arreglar tu habitación no te voy a dar nada.")

else:
    print("Debes elegir una opción correcta.")