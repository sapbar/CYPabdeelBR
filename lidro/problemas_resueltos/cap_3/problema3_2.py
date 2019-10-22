sumser = 0
band = 't'
i = 2
for i  in range ( 1, 1801 ,1):
    sumser += 1
    print(f" {i}")
    if band == 't':
        band = 'f'
        i += 3
    else:
        band ='t'
        i +=2
print("", sumser)
