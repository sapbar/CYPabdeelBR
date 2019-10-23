nom = 0
while (sue != -1):
    sue=float(input("sueldo :"))
    if  sue < 1000:
        nsue = sue * 1.15
    else:
        nsue = sue *1.12
  nom += nsue
  print (f"nuevo sueldo {nsue}")

