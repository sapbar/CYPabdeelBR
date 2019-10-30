n = int(input("ingrese el numero de el elementos del arreglo:"))
vec =[]
if n >= 1 and n <=500:
    #logica
    for i in range(0,n,1):
        vec.append(int(input("ingresa valor :")))
    vec.sort()
        print("lista de numeros sin repeticiones:")
        i = 0
        while i <= n-1:
            print(vec[i])
            REPET=vec[i]
            while i <= n and REPET==vec[i]:
                i +=1
else:
    print("el numero de elementos del arreglo es incorrecto")

