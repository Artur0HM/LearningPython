# Para ayudar a un trabajador a saber cuál será su sueldo semanal, se sabe que si trabaja 40 horas o menos, se le pagará $20 por hora, pero si trabaja más de 40 horas entonces las horas extras se le pagarán a $25 por hora.



horas_trabajadas = int(input("Cuantas horas trabajaste esta semana: "))

pago_por_hora               = 20
pago_por_hora_extra         = 25
horas_trabajadas_por_semana = 40

if horas_trabajadas == 1:
    print("Esta semana trabajaste", horas_trabajadas , "hora, esta semana recibiras:", horas_trabajadas * pago_por_hora , "dolares.")

elif horas_trabajadas <= 40:
    print("Esta semana trabajaste", horas_trabajadas , "horas, esta semana recibiras:", horas_trabajadas * pago_por_hora , "dolares.")

elif horas_trabajadas > 40:
    print("Esta semana trabajaste un total de", horas_trabajadas , "horas.") 
    print("Horas extras trabajadas esta semana" , horas_trabajadas - horas_trabajadas_por_semana, "horas.")
    print("Por tus horas extras recibiras un pago de", pago_por_hora_extra , "dolares por hora, por tus",horas_trabajadas - horas_trabajadas_por_semana, "horas, recibiras un pago extra de", (horas_trabajadas - horas_trabajadas_por_semana) * pago_por_hora_extra)
    print("Total a pagar esta semana es de:", (horas_trabajadas_por_semana * pago_por_hora) + ((horas_trabajadas - horas_trabajadas_por_semana) * pago_por_hora_extra))

else:
    print("Debes elegir ingresar un número.")