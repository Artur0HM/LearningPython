# El testigo hablará siempre que le garanticen protección.

testigo = """
EL TESTIGO HABLARA MIENTRA LE GARANTICEN PROTECIÓN

1 - SI
2 - NO

DEBES ESCOGER UNA OPCIÓN: """

declarar = int(input(testigo))

if declarar == 1:
    print("El jusgado le promete protección")

elif declarar == 2:
    print("El jusgado no le garantiza protección.")

else:
    print("Debes escoger una opción correcta.")