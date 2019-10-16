print("sueldo de oras extras")
cat = int(input("incerte la categoria :"))
he = int(input("cantidad de horas extras :"))
sue = int(input("sueldo actual :"))
if cat == 1:
    phe = 30
elif cat == 2:
    phe = 38
elif cat == 3:
    phe = 50
elif cat ==  4:
    phe = 70
else:
    phe = 0
if he > 30:
    nsue = sue +30 *phe
else:
    nsue = sue + he * phe
print(f"sueldo con comicion por horas extras es de : {nsue}")


