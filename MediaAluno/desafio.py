n1,n2,n3,n4 = [float(x) for x in input().strip().split(" ")]

media = (n1*2 + n2*3 + n3*4 + n4)/10

print(f"Media: {media:.1f}")

if media >=7:
    print("Aluno aprovado.")
elif media >=5 and media <=6.9:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame)/2
    if media_final >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")
else:
    print("Aluno reprovado.")

