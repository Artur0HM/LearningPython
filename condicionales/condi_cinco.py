# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# 
#       Renta	             Tipo impositivo
# Menos de 10000€	                5%
# Entre 10000€ y    20000€	        15%
# Entre 20000€ y 35000€	            20%
# Entre 35000€ y 60000€	            30%
# Más de 60000€	                    45%

# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.


ingresos = float(input("De caunto es tu ingreso anual: "))
#ingresos = str(ingresos)
impuesto_uno = 5
impuesto_dos = 15
impuesto_tres = 20
impuesto_cuatro = 30
impuesto_cinco = 45



if  ingresos < 10000:
    print("Tus ingresos anuales es de", ingresos, "dolares, debes pagar el 5%")
    print("Tienes que pagar: ", ingresos * impuesto_uno / 100, "$")
    

elif ingresos < 20000:
    print("Tus ingresos anuales es de", ingresos, "dolares, debes pagar el 15%")
    print("Tienes que pagar: ", ingresos * impuesto_uno / 100, "$")

    
elif ingresos < 35000:
    print("Tus ingresos anuales es de", ingresos, "dolares, debes pagar el 20%")
    print("Tienes que pagar: ", ingresos * impuesto_uno / 100, "$")
    
elif ingresos < 60000:
    print("Tus ingresos anuales es de", ingresos, "dolares, debes pagar el 30%")
    print("Tienes que pagar: ", ingresos * impuesto_uno / 100, "$")
    
else:
    print("Tus ingresos anuales es de", ingresos, "dolares, debes pagar el 45%")
    print("Tienes que pagar: ", ingresos * impuesto_uno / 100, "$")
        
