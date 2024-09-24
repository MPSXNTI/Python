# -*- coding: utf-8 -*-

dia_nac = int(input("Ingrese el dia de nacimiento: "))
mes_nac = int(input("Ingrese el mes de nacimiento: "))
anio_nac = int(input("Ingrese el año de nacimiento: "))

dia_actual = int(input("Ingrese el dia actual: "))
mes_actual = int(input("Ingrese el mes actual: "))
anio_actual = int(input("Ingrese el año actual: "))

anio_exac = anio_actual - anio_nac
mes_exac = mes_actual - mes_nac
dia_exac = dia_actual - dia_nac

if dia_exac < 0:
    dia_exac += 30
    mes_exac -= 1
if mes_exac < 0:
    mes_exac += 12
    anio_exac -= 1

print("La edad exacta es:", anio_exac, "año(s)", mes_exac, "mes(es)", dia_exac, "día(s)")