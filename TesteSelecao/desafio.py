a,b,c,d = [int(x) for x in input().strip().split(" ")]

if b > c and d>a  and c+d>a+b and (c and d >=0) and a%2 ==0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos") 