serie=0
n=int(input("dame un mumero entero :"))
band= 'T'
i= 1
while (i <= n):
    if band == 'T':
    serie =  serie +1/i
    band ='F'
    else:
        serie =  serie -1/i
        band='T'

print(serie)


