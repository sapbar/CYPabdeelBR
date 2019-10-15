cuecer=0
n= int(input("dame un numero entero positivo :"))
for I in range(1,n,1):
    num=int(input("ingresa un entero :"))
    if num == 0:
        cuecer += 1
print("el numero de 0's capturaos fue:", cuecer)


