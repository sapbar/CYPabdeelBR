#print tiene 4 formas de uso

"""
1.-con comas
2.- con signo '+'
3.-con la funcion format()
4.-es con una variable de format()
"""
#con comas
#un espacio y haciendo casting de tipo
edad=10
nombre='sarid'
estatura=1.87
print(edad , estatura , nombre)

#con signo mas hace lo mismo pero no hace el casting automatico, no agrega espacio
#hace una concatenacion
print(str (edad)+ str (estatura) + nombre)

#con la funcion format()
print ("nombre: {1} edad: {0}".format(edad, nombre))

#la forma 4 es una bariante de format de forma simplificada

print(f"Nombre: \"{nombre}\" \nEdad:\t{edad}")
# print y el argumento end

print("solo hay dies tipos de personas las que saben binario y las que no ", end="")
print("otra linea")
