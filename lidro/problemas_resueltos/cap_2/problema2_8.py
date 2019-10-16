print("descunto en compras")
des=0
com = float(input("introduce el monto de la compra :"))
if com < 500:
    print(f"no  hay descunto el monto a pagar es: {des}")
else :
    if com > 500 <= 1000:
        des = com - com * 0.05 
        print(f"el monto a pagar con descunto es :{des}")
    elif  com > 1000 <= 7000:
        des = com - com *  0.11
        print(f"el monto a pagar con descunto es :{des}")
    elif com > 7000 <= 15000:
        des = con - com * 0.18
        print(f"el monto a pagar con descunto es :{des}")
    else:
        des = com - com * 0.25
        print(f"el monto a pagar con descunto es :{des}")
print("fin del programa")


