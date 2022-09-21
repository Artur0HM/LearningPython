#  para una tienda de zapatos que tiene una promoción de descuento para vender al mayor, esta dependerá del número de zapatos que se compren. Si son más de diez, se les dará un 10% de descuento sobre el total de la compra; si el número de zapatos es mayor de veinte pero menor de treinta, se le otorga un 20% de descuento; y si son más treinta zapatos se otorgará un 40% de descuento. El precio de cada zapato es de $80.

numero_zapatos = int(input("Cuantos zapatos compro: "))

primer_descuento    = 10
segundo_descuento   = 20
tercer_descuento    = 40
precio_del_zapato   = 80

if numero_zapatos <= 10:
    print("Compraste", numero_zapatos , "zapatos.")
    print("Cada zapato tiene un precio de", precio_del_zapato , "dolares.")
    print("Total a pagar por los", numero_zapatos , " zapatoz es: ", numero_zapatos * precio_del_zapato)

elif numero_zapatos > 10 or numero_zapatos <= 20:
    print("Compraste", numero_zapatos , "zapatos.")
    print("Cada zapato tiene un precio de", precio_del_zapato , "dolares.")
    print("total a pagar por los", numero_zapatos , "zapatos es:", numero_zapatos * precio_del_zapato)
    print("tienes un descuento de", primer_descuento, "% nuevo total a pagar es:", ((numero_zapatos * precio_del_zapato) - (numero_zapatos * precio_del_zapato)  * primer_descuento /100), "dolares.")

elif numero_zapatos > 20 or numero_zapatos <= 30:
    print("Compraste", numero_zapatos , "zapatos.")
    print("Cada zapato tiene un precio de", precio_del_zapato , "dolares.")
    print("total a pagar por los", numero_zapatos , "zapatos es:", numero_zapatos * precio_del_zapato)
    print("tienes un descuento de", segundo_descuento, "% nuevo total a pagar es:", ((numero_zapatos * precio_del_zapato) - (numero_zapatos * precio_del_zapato)  * segundo_descuento /100), "dolares.")

elif numero_zapatos > 30:
    print("Compraste", numero_zapatos , "zapatos.")
    print("Cada zapato tiene un precio de", precio_del_zapato , "dolares.")
    print("total a pagar por los", numero_zapatos , "zapatos es:", numero_zapatos * precio_del_zapato)
    print("tienes un descuento de", tercer_descuento, "% nuevo total a pagar es:", ((numero_zapatos * precio_del_zapato) - (numero_zapatos * precio_del_zapato)  * tercer_descuento /100), "dolares.")

else:
    print("DEBES INGRESAR UN NÚMERO ENTERO.S")