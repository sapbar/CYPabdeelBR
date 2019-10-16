imp = 0
bas = float(input("dame el precio base del producto :"))
if bas > 500:
    imp =  20 * 0.30 + (bas-40) * 0.50  
elif  bas > 40:
     imp = 20 * 0.30 + (bas - 40) * 0.40
elif bas > 20:
    imp = 20 * 0.30 + (bas - 40) * 0.30
else:
    imp = 0
tota = bas + imp
print(f"el precio  base del producto es {bas} y con el impuesto aplicado  es de : {tota}")

