def sumar (x , y):
    z = x + y
    return z
def restar (x , y):
    z= x - y
    return x -y
def mi_print(texto):
    print(f"Este es mi print :{texto}")

def multiplica(valor , veces):
    if veces == None:
        print("debes enviar el segundo argumento de la funcion")
    else:
        print(valor * veces)
def comanda(mesa, comensal , entrada , medio , fuerte , postre="gelatina de limon"):
    print(f"mesa: {meas} comensal:{comensal}")
    print(f"\t entrada:{entrada}")
    print(f"\t segundo tiempo: {medio}")
    print(f"\t plato fuerte: {fuerte}")
    print(f"\t postre: {postre}")
def imprime_argumentos(*aegumentos):
    for index in range(len(argumentos)):
    print(argumentos[index])
def comanda2(**comida):
    print(comida)

    a=10
    b=5
    c= sumar (a,b)
    print(f"la suama de {a} mas  {b} es {c}")
    c= restar(a,b)
    print(f"la resta de {a} y {b} es {c}")
    multiplica(10 , 3)
    multiplica(10, None)
    multiplica('hola', 3)
    comanda(2,1, "entrada","sopa de rana","filete de pompi de sirena", "flan")
    comanda( "entrada","sopa de rana","filete de pompi de sirena", "flan",2,1)
    comanda( "entrada","sopa de rana","filete de pompi de sirena", ,2,1)
    imprime_argumentos('hola',True, 3.1416,1000,{'id':'sc01','nombre':'juan'})
     comanda( "entrada","sopa de rana","filete de pompi de sirena", ,2,1)
 

