def pertenece (s:list, x:int) -> bool:
    for elem in s:
        if elem == x:
            return True
    return False

print(pertenece([1,2,3,4],4))
print(pertenece([1,2,3,4],5))

print("--------------------------------")

def divideAtodos (s:list, x:int) -> bool:
    for i in s:
        if i%x !=0:
            return False
    return True

print(divideAtodos([1,2,3,4],1))
print(divideAtodos([1,2,3,4],2))

print("--------------------------------")

def sumaTotal (s:list) -> int:
    res = 0
    for elem in s:
        res = res + elem
    return res

print(sumaTotal([1,2,3,4,5]))

print("--------------------------------")

def ordenados (s:list) -> bool:
    res = s[0]-1
    for i in s:
        if i > res:
            res=i
        else: 
            return False
    return True

print(ordenados([1,2,3,4,5]))
print(ordenados([1,2,3,5,4]))

print("--------------------------------")

def palabrasLargas (x:list) -> bool:
    for i in x:
        if len(i)>7:
            return True
    return False

print(palabrasLargas(["Hola", "me", "llamo", "Juanchissssssss"]))

print("--------------------------------")

def palindroma (palabra: str) -> bool:
    adelante=0
    atras=len(palabra)-1
    while adelante != atras:
        if palabra[adelante] == palabra[atras]:
            adelante += 1
            atras -= 1
        else:
            return False
    return True

print(palindroma("neuquen"))
print(palindroma("kiosco"))

print("--------------------------------")

def analisisContraseña (contraseña:str) -> str:
    letra = 0
    minuscula = 0
    mayuscula = 0
    numero = 0

    if len(contraseña) < 5:
        return "ROJO"
    while letra < len(contraseña):
        if not("a" <= contraseña[letra] <= "z") and not("A" <= contraseña[letra] <= "Z") and ("0" <= contraseña[letra] <= "9"): 
            letra += 1
            numero += 1
        elif not("a" <= contraseña[letra] <= "z") and "A" <= contraseña[letra] <= "Z":
            letra += 1
            mayuscula += 1
        elif "a" <= contraseña[letra] <= "z":
            letra += 1
            minuscula += 1
        else: letra += 1
    if (numero==0) or (mayuscula==0) or (minuscula==0):
        return "AMARILLO"
    else:
        return "VERDE"


print(analisisContraseña("Holfdsfda1"))
print(analisisContraseña("Hola"))
print(analisisContraseña("Holaadasasddas"))
print(analisisContraseña("&/(&#!%!%!%!%!)"))



