cat=int(input("introduce una categoria (1-4) :"))
sue=float(input("intriduce sueldo actual :"))
nsue=0
if cat == 1 :
    nsue= sue * 1.15
elif cat == 2 :
    nsue = sue * 1.10
elif cat == 3 :
    nsue = sue * 1.08
elif cat == 4 :
    nsue = sue * 1.07

print(f"Al ser categoria {cat} tu nuevo sueldo es : {nsue}")
print("fin del programa")

