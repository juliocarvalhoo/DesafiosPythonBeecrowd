valor = float(f"{float(input()):.2f}")

notas = [100,50,20,10,5,2]
moedas = [1,0.5,0.25,0.10,0.05,0.01]

notaSaida = []
moedaSaida = []

for i,element in enumerate(notas):
    notaSaida.append(valor // element)
    valor = valor % element
    if element == 2:
        for i, element in enumerate(moedas):
            moedaSaida.append(valor // element)
            valor = valor % element
            
listaZip = zip(notaSaida,notas)       
moedasZip = zip(moedaSaida,moedas)      
     
print("NOTAS:")
for valor in listaZip:
    print(f"{valor[0]:.0f} nota(s) de R$ {valor[1]:.2f}")
print("MOEDAS:")
for valor in moedasZip:
    print(f"{valor[0]:.0f} moeda(s) de R$ {valor[1]:.2f}")
