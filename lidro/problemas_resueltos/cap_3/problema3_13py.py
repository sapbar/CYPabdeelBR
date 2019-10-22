arsu = 0
arno = 0
mersu = 50000
mes = 0
arce = 0
for i in range(1 , 13 , 1):
    print(f"mes : {i}")
    rno = int(input ("promedio de lluvias del mes zona norte :"))
    rce = int(input ("promedio de lluvias del mes zona centro :"))
    rsu = int(input ("promedio de lluvias del mes zona sur :"))

    arno = arno + rno
    arce = arce + rce
    arsu = arsu + rsu

    if rsu < mersu:
        mersu = rsu
        mes = i
prorce = arce / 12
print(f"promrdio region centro : {prorce} ")
print(f"Mes con menor lluvia de reg. sur : {mes}")
print(f"region del mes con menor lluvia es : {mersu}")


if arno > arce:
    if arno > arsu:
        print("La region con mayor lluvia es la region norte")
    else:
        print("La region con mayor lluvia es la region sur")
elif arce > arsu:
    print("La region con mayor lluvias es la del centro")
else:
    print("La region con mayor lluvia es la region sur")

print("fin del programa")
