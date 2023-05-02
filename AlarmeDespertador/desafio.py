h1,m1,h2,m2 = [int(x) for x in input().strip().split(" ")]

x1_minutos = h1*60 + m1
x2_minutos = h2*60 + m2


if x2_minutos > x1_minutos:
    minutos_descanso = x2_minutos - x1_minutos
    print(minutos_descanso)
    
elif x1_minutos == x2_minutos:
    pass

else:
    minutos_descanso = x2_minutos + (24*60) - x1_minutos
    print(minutos_descanso)











