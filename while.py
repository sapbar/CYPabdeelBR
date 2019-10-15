otra =  bool(int(input("hay mas alumnos (0 para no, 1 para si):")))
suma = 0.0
cont = 0
while(otra == True):
    cal = float(input("callificacion :"))
    cont += 1
    suma += cal
    otra = bool(int(input("hay mas alumnos (0 para no, 1 para si):")))
print("suma",suma)
print("promedio :", suma / cont)
print("fin del programa")

