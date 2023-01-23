import time

# %H = formateo de 24h
# %M = obtiene minutos

def hora_salida():
    hora = time.strftime('%H') 
    minutos = time.strftime('%M') 

# int() convierte la hora a número entero
    if int(hora) >= 19:
        print("Es hora de irse a casa")
# Supongamos que son las 15:00; hace la siguiente resta: 18,59 - 15,00 = 3,59 (falta 3:59 para las 19:00)
# El último minúto no se pone porque la condición if incluye "= a 19" por lo tanto fallaría el else
    else:
        print("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))
        
hora_salida()