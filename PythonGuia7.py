
from math import sqrt, floor, ceil
def raizDe2():
   return round (sqrt(2), 4)
    
#print(raizDe2())

def  imprimir_hola():
    print ("Hola")

def imprimir_un_verso():
    print ("te estas portando mal")
    print ("seras castigada")

def factorial_de(n: int) -> int:
    x: int = n
    y: int = 1
    while x >= 1 :
        y = y*x
        x = x-1
    
    return y


def es_multiplo_de_1(n: int, m: int) -> bool:
    res: bool
    if n % m == 0:
        res = True
    else:
        res = False
#n%m es n mod m
    return res

def es_multiplo_de_2(n: int, m: int) -> bool:
    if n % m == 0:
        return True
    else:
        return False
#n%m es n mod m

#es_multiplo_de_1 es la mejor respecto de la correctitud del codigo

def es_multiplo_de_sin_if(n: int, m: int) -> bool:
    res: bool = n%m == 0
    return res

def es_multiplo_de_sin_if_sin_res(n: int, m: int) -> bool:
    return n%m == 0

print (es_multiplo_de_1 (5,1))
print (es_multiplo_de_2 (70,10))
print (es_multiplo_de_sin_if (70,10))
print (es_multiplo_de_sin_if_sin_res (70,10))