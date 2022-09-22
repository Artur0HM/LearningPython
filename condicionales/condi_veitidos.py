# Para determinar el aumento de un trabajador, se debe tomar en cuenta que si ganaba más de $2000 tendrá un aumento del 5%, si generaba menos de $2000 su aumento será de un 10%.

cuanto_gamas_al_mes = int(input("Ingrese el monto que gana al mes: "))
primer_aumento  = 5
segundo_aumento = 10


if cuanto_gamas_al_mes > 2000:
    print("Al mes ganas", cuanto_gamas_al_mes , "dolares, tendras un aumento del", primer_aumento ,"%")
    print("Este mes ganaras", (cuanto_gamas_al_mes * primer_aumento / 100) + cuanto_gamas_al_mes , "dolares.")

elif cuanto_gamas_al_mes <= 2000:
    print("Al mes ganas", cuanto_gamas_al_mes , "dolares, tendras un aumento del", segundo_aumento ,"%")
    print("Este mes ganaras", (cuanto_gamas_al_mes * segundo_aumento / 100) + cuanto_gamas_al_mes , "dolares.")

else:
    print("Debes ingresar números.")