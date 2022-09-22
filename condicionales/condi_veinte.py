# Para una tienda de helado da un descuento por compra a sus clientes con membresía dependiendo de su tipo, sólo existen tres tipos de membresía, tipo A, tipo B y tipo C. Los descuentos son los siguientes:

# Tipo A 10% de descuento
# Tipo B 15% de descuento
# Tipo C 20% de descuento

membresia = """
Que membresia estas inscrito:

1 - Tipo A
2 - Tipo B
3 - Tipo C

Escoge una opción: """
tipo = int(input(membresia))
descuento_tipo_a = 10
descuento_tipo_b = 15
descuento_tipo_c = 20

if tipo == 1:
    print("Tu membresia es de TIPO A, tienes un descuento del", descuento_tipo_a, "%.")

elif tipo == 2:
    print("Tu membresia es de TIPO B, tienes un descuento del", descuento_tipo_b, "%.")

elif tipo == 3:
    print("Tu membresia es de TIPO C, tienes un descuento del", descuento_tipo_c, "%.")

else:
    print("Debes escoger una opción correcta.")
