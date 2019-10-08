num=int(input("ingresa un numero entero positivo :"))
v=int(input("ingresa otro unmero entero positivo :"))
val=0
if num == 1 :
    val= 100 * v
elif num == 2 :
    val= 100 ** v
elif num == 3 :
    val= 100 / v
else: 
    val= 0

print(f"El resultado es {val}")
print("fin del programa")
 
