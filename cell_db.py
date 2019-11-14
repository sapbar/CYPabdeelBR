#cell_db.py
def leer_datos(path):
    file=open(path ,'rt')
    lista_final=[]
    dic_cel={}
    datos= file.readlines()
    for ren in range(len(datos)):
        datos[ren]=datos[ren].strip(',')
    #print(datos)
    for ren in range(1,len(datos),1):
        dic_cel={}
        for col in range(0,len(datos)):
            dic_cel[datos[0][col].strip()]=datos[ren][col]
        lista_final.append(dic_cel)
    return lista_final
def salida_formato (celular):
    print(f"\t celular marca { celular['marca'] }")
    print(f"\t modelo: {celular['modelo']}")
    print(f"\t almacenamiento: {celular['almacenamiento']}")
    print(f"\t velocidad: {celular['velocidad']}")
    print(f"\t ram: {celular['ram']}")
    print(f"\t color: {celular['color']}")
def main():
    archivo = "celulares.txt"
    bd = leer_datos(archivo)
    print(f"BD={bd}")
    salida_formato(bd[6])
    
main()
