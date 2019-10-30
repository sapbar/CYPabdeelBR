# arreglos
#lectura
#escritura / asignacion
#actualizacion: insercion, elininacion, modificacion
#ordenamiento
#busqueda

#escritura
frutas = ["zapote","manzana","pera","aguacate","durazno","uva","sandia"]

#lectura, el selector [indice]
print(frutas [2])
#lectura con for
#for opcion 1
for indice in range(0,7,1):
    print(frutas[indice])
print("------------------")
#for opcion 2 -- por un iterador for each

for fr in frutas:
    print(fr)
#asignacion
frutas [2] ="melon"
print(frutas)

#insercion al final
frutas.append("naranja")
print(frutas)
print(len(frutas))
frutas.insert(2,"limon")
print(frutas)
print(len(frutas))
frutas.insert(0, "mamey")
print(frutas)

#eliminacion con pop
print(frutas.pop())
print (frutas)
print(frutas.pop(1))
print (frutas)
frutas[2] ="limon"
frutas.append("limon")
frutas.append("limon")
print(frutas)
frutas.remove("limon")
print(frutas)

#ordenaminto
frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

#busqueda
print(f"el uva esta em la posicion {frutas.index('uva')}")

print(f"el limon esta {frutas.count('limon')} veces en la lista")

#contactar
print(frutas)
otras_frutas= ["rambutan","nispero","liche","pitahaya"]
frutas.extend(otras_frutas)
print(frutas)

#copiar
otra_copia = frutas.copy()
otra_copia.append("fresa")
otra_copia.append("fresa")
print(frutas)
print(otra_copia)

