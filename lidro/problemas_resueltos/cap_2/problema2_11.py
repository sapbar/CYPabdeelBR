print("costo de llamadas")
cost = 0
clave = int(input("proporcionar clave de larga distancia :"))
nmin = int(input("tiempo de la llamada en minutos :"))
if clave == 12:
    cost = nmin * 2
elif clave == 15 :
    cost = nmin * 2.2
elif clave == 18 :
    cost = nmin *  4.5
elif clave == 19 :
    cost = nmin * 3.5
elif clave == 23 or 25:
    cost = nmin * 6
else:
    clave == 29.
    cost = nmin * 5
print(f" para la clave {clave} y por una llamada de {nmin} el costo es de: {cost}")

