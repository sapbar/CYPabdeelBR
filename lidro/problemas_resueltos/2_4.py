sue=float(input("cual es el sueldo deel trabajador? :"))

if sue < 1000:
    nsue= (sue * 0.15) + sue
    print(f" El nuevo sueldo es {nsue}")
else:
    
    nsu= (sue * 0.12) + sue
    print(f" El nuevo sueldo es {nsu}")
