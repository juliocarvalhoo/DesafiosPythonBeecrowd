'''Treinando uso de dictionary'''

numeroEntrada = int(input())
contador = 0

dictRepe = {}

while contador != numeroEntrada:
    x = int(input())
    if str(x) not in dictRepe:
        dictRepe[str(x)] = 1
    else:
        dictRepe[str(x)] = dictRepe[str(x)] + 1
        
    contador +=1

dicionario_ordenado = dict(sorted(dictRepe.items()))
[print(f"{x} aparece {y} vez(es)") for x,y in dicionario_ordenado.items()]




    

    