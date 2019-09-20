print("El area de un triangulo en base a sus lados")
L1= float(input("Dame el lado uno :"))
L2= float(input("Dame el lado dos :"))
L3= float(input("Dame el lado tres :"))
s= (L1 +  L2 + L3)/2
area= (s*(s-L1)*(s-L2)*(s-L3))**0.5

print(f"el area del triangulo es {area} Y EL CALCULO AUXILIAR ES IGUAL A {s}")


