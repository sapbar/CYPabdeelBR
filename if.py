edad= int(input("dame tu edad:"))
INE = bool(int(input("tienes ine (0 no / 1 si):"))) 
if edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("aun dentro de if")
print("fin del programa")

