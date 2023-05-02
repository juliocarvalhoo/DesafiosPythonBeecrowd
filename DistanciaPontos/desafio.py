from math import sqrt
x1,y1 = [float(x) for x in input().strip().split(" ")]
x2,y2 = [float(x) for x in input().strip().split(" ")]

distancia = sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print(f"{distancia:.4f}")