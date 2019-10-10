a=int(input("introbuce un valor entero positivo : "))
b=int(input("introduce otro valor entero :"))
c=int(input("introduce otro valor entero :"))
if a > b:
    if a > c:
        print(f"a es un valor con mayor a {a}")
    elif a== c:
        print(f"a y c son iguales a {a} y son los mayores")
    else:
        print(f" c que vale {c} es el mayor")
elif a == b:
    if a > c:
        print(f"a y b con los mayor con valor {b}")
    elif a== c:
        print(f"los tres son iguales a {b}")
    else:
        print(f"c que vale {c} es mayor")
elif b > c:
    print(f" b que vale {b} es mayor")
elif b==c:
    print(f"b y c son los mayores con valor {c}")
else:
    print(f"c es el mayor con valor {c}")
print("fin del programa")

