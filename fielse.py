edad=int(input("dame tu edad:"))
ine = bool(int(input("tienes ine (0 no / 1 si)?:")))

if edad >= 18 and ine == True:
    print("eres mator de edad")
    print("puedes entrar al bar")
else:
    print("Eres menor de edad")
    print("Puedes ir a la chosa de los pequeñines")

print("fin del programa")

