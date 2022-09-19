# En un almacén se descuenta 20% del precio al cliente si el valor a pagarse es mayor a $200. Dado un valor de precio, muestre lo que debe pagar el cliente.

cuenta_del_cliente = float(input("Ingrese cantidad a cobrar: "))
porcentaje_descuento = 20
total_pagar = cuenta_del_cliente * porcentaje_descuento / 100

if cuenta_del_cliente <= 200:
    print("Debera pagar: ", cuenta_del_cliente , "dolares.")

elif cuenta_del_cliente > 200:
    print("Los productos que compro superan los", cuenta_del_cliente , "dolares, le corresponde un descuento del", porcentaje_descuento, "%, total a pagar es", cuenta_del_cliente - porcentaje_descuento , "dolares.")