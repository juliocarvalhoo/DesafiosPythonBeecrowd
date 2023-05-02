import math


'''Utilizando list comprehension v'''
# a, b, c = [float(x) for x in input().strip().split(' ')]

entrada = input()
listaEntrada = entrada.split(" ")
a=float(listaEntrada[0])
b=float(listaEntrada[1])
c=float(listaEntrada[2])

delta = (b**2)-4*a*c

if delta > 0:
    try:
        r1 = (-b+(math.sqrt(delta)))/(2*a)
        r2 = (-b-(math.sqrt(delta)))/(2*a)
        print(f"R1 = {r1:.5f}")
        print(f"R2 = {r2:.5f}")
    except ZeroDivisionError as divisao:
        print("Impossivel calcular")
else:
    if delta ==0:
        try:
            r1=-b/2*a
            r2=-b/2*a
            print(f"R1 = {r1:.5f}")
            print(f"R2 = {r2:.5f}")
            #MESMO VALOR
        except ZeroDivisionError as divisao:
            print("Impossivel calcular")
    else:
        print("Impossivel calcular")
            

            
    
        
    