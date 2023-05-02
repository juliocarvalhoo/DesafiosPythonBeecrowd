from math import pi

a, b, c = [float(x) for x in input().strip().split(" ")]

# a = base    c = altura
def areaTrianguloRetangulo(a,c):
        print(f"TRIANGULO: {(a*c)/2:.3f}")
# c = raio
def areaCirculo(c):
    print(f"CIRCULO: {pi*(c**2):.3f}")
# a,b = bases   c=altura
def areaTrapezio(a,b,c):
    print(f"TRAPEZIO: {((a+b)*c)/2:.3f}")
# b= lado
def areaQuadrado(b):
    print(f"QUADRADO: {b*b:.3f}")
# a,b = lados
def areaRetangulo(a,b):
    print(f"RETANGULO: {a*b:.3f}")
    
areaTrianguloRetangulo(a,c)
areaCirculo(c)
areaTrapezio(a,b,c)
areaQuadrado(b)
areaRetangulo(a,b)
    
        