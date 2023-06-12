#ARCHIVOS
#ejercicio1
import random
def contarlineas(nombre_archivo:str)->int:
    i:int = 0
    archivo:str= open(nombre_archivo, 'r')
    for linea in archivo:
        i= i+1
    archivo.close()
    return i
#test = 'archivos/test.txt'
#cantidad_lineas = contarlineas(test)
#print("Cantidad de líneas:", cantidad_lineas)

def existePalabra(palabra:str, nombre_archivo:str)->bool:
    archivo:str= open(nombre_archivo, 'r')
    for linea in archivo:
        if palabra in linea:
            return True
    archivo.close()
    return False

#palabra= "Bienvenide"
#existe_palabra = existePalabra(palabra,test)
#print("esta",palabra,"?", existe_palabra)

def cantidadApariciones(nombre_archivo:str,palabra:str)->int:
    i:int=0
    archivo:str=open(nombre_archivo,'r')
    for linea in archivo:
        if palabra in linea:
           i=i+1
    archivo.close
    return i 
#archivo1 = "archivos/hola1.txt"
#ejercicio2
def crearArchivo(nombre_archivo:str):
    archivo = open(nombre_archivo, 'w')
    archivo.close()

#crearArchivo(archivo1)
def crear_ruta(nombre_archivo:str)-> str:
    res= "archivos/"+nombre_archivo
    return res

def clonarSinComentarios(nombre_archivo:str):
    ruta_archivo:str=crear_ruta(nombre_archivo)
    archivo:str=open(ruta_archivo,'r')
    ruta_archivosc:str=crear_ruta(nombre_archivo + "sc")
    crearArchivo(ruta_archivosc)
    archivosc:str=open(ruta_archivosc,'w')
    for linea in archivo:
        i:int=0
        while i<len(linea)-1:
            if linea[i] != "#" and linea [i]!=" ":
                archivosc.write(linea)
                i=i+len(linea)
            else:
                if linea [i] == " ":
                    i=i+1
                if linea [i] == "#":
                    i=1+len(linea)
    archivo.close()
    archivosc.close()
#test1 = "test.txt"
#clonarSinComentarios(test1)

def addtxt(nombre_archivo:str)->str:
    res= nombre_archivo +".txt"
    return res

def addexe(nombre_archivo:str)->str:
    res= nombre_archivo +".exe"
    return res

#ejercicio3
def archivoReverso(nombre_archivo:str):
    ruta_archivo:str=crear_ruta(addtxt(nombre_archivo))
    ruta_archivorvs:str=crear_ruta(addtxt(nombre_archivo+"rvs"))
    archivo:str= open(ruta_archivo,'r')
    archivorvs:str= open(ruta_archivorvs, 'w')
    lineas:list=archivo.readlines()
    i:int=len(lineas)-1
    while i>=0:
        archivorvs.write(lineas[i]+"\n")
        i=i-1
    archivo.close()
    archivorvs.close()

archivo="test"
#archivoReverso(archivo)

#ejercicio 4
#esta funcion reescribe el archivo y le agrega la frase al final, se puede hacer mas facil con modo 'a' "modo append"
def agregarFraseFinal(nombre_archivo:str,linea_nueva:str):
    ruta_archivo:str=crear_ruta(addtxt(nombre_archivo))
    archivo:str = open(ruta_archivo,'r')
    lineas_anteriores:list=archivo.readlines()
    archivo.close()
    archivo:str = open(ruta_archivo, 'w')
    for i in lineas_anteriores:
        archivo.write(i)
    archivo.write("\n")
    archivo.write(linea_nueva+"\n")
    archivo.close()

#agregarFraseFinal(archivo,"titi boludo")

#ejercicio 5
def agregarFrasePrincipio(nombre_archivo:str,linea_nueva:str):
    ruta_archivo:str=crear_ruta(addtxt(nombre_archivo))
    archivo:str = open(ruta_archivo,'r')
    lineas_anteriores:list=archivo.readlines()
    archivo.close()
    archivo:str = open(ruta_archivo, 'w')
    archivo.write(linea_nueva+"\n")
    for i in lineas_anteriores:
        archivo.write(i)
    archivo.close()

#agregarFrasePrincipio(archivo,"titi boludo")
#ejercicio 6
def obtener_palabras_legibles(nombre_archivo:str):
    ruta_archivo:str=crear_ruta(addexe(nombre_archivo))
    archivo:str = open(ruta_archivo,'rb')
    palabras_legibles = []
    for linea in archivo.readlines():
        linea_texto = linea.decode('utf-8')
        palabras = linea_texto.split()
        for palabra in palabras:
            if len(palabra) >= 5 and palabra.isalnum() and palabra.isalpha():
                palabras_legibles.append(palabra)
    archivo.close()
    return palabras_legibles
#ejercicio 7
def promedioEstudiante(lu: str) -> float:
    archivo:str = open("nombre_archivo.csv", "r")
    suma_notas:int=0
    cantidad_notas:int=0
    for linea in archivo.readlines():
        campos = linea.split(",")
        if campos[0] == lu:
            nota=campos[3]
            suma_notas = suma_notas + nota
            cantidad_notas = cantidad_notas + 1
    archivo.close()
    if cantidad_notas > 0:
        promedio_final= suma_notas/cantidad_notas
        return promedio_final
    else:
        return -1 #valor para indicar que no hay notas disponibles


#PILAS
#ejercicio 8
def generarNrosAlAzar(n:int,desde:int,hasta:int)->list[int]:
    i:list[int] = range(desde,hasta,1)
    res= random.sample(i,n)
    return res
#print(generarNrosAlAzar(5,2,8))

#ejercicio9
import queue
from queue import LifoQueue as Pila
#p= Pila()
#p.put(1) (apila el 1)
#elemento = p.get() desapilar
#p.empty() esta vacia?

def pila_random(n:int,desde:int,hasta:int)->Pila:
    p:Pila = Pila()
    lista_num_random:list[int] = generarNrosAlAzar(n,desde,hasta)
    for i in lista_num_random:
        p.put(i)
    return p

#ejercicio 10

def cantidadElementos(p:Pila)->int:
    count:int = 0
    p_aux:Pila = Pila()

    while not p.empty():
        elemento = p.get()
        p_aux.put(elemento)
        count+=1
    while not p_aux.empty():
        elemento = p_aux.get()
        p.put(elemento)
    return count

#ejercicio11

def pila_da_lista(p:Pila)->list:
    l:list=[]
    p_aux:Pila =Pila()
    while not p.empty():
        elem=p.get()
        l.append(elem)
        p_aux.put(elem)
    while not p_aux.empty():
        elem = p_aux.get()
        p.put(elem)
    return l

def buscarElMaximoEnLaPila(p:Pila)->int:
    lista:list=pila_da_lista(p)
    res:int=max(lista)
    return res
#pila = Pila()
#pila.put(5)
#pila.put(2)
#pila.put(8)
#pila.put(3)

#maximo = buscarElMaximo(pila)
#print("Maximo valor en la pila:", maximo)

#ejercicio 12

def tope(p:Pila):
    if not p.empty():
        elem = p.get()
        p.put(elem)
        return elem
    return None


def estaBienBalanceada(s:str)->bool:
    p:Pila = Pila()
    elem = None #valor predeterminado
    for char in s:
        if char =='(':
            p.put(char)
        else:
            if char == ')':
                elem = tope(p)
                if p.empty() or elem != '(':
                    return False
                p.get()
    return p.empty()

#formula1 = '1 + (2 x 3 = (20 / 5))'
#formula2 = "10 * (1 + (2 * (=1)))"
#formula3 = '1 + ) 2 x 3 ( ( )'

#print(estaBienBalanceada(formula1))  # Salida: True
#print(estaBienBalanceada(formula2))  # Salida: True
#print(estaBienBalanceada(formula3))  # Salida: False

#COLAS
#ejercicio13
from queue import Queue as Cola
#c=Cola()
#c.put(1) encolar 1
#elem=c.get() toma el ultimo lo guarda en la variable elem y lo borra de la cola
#c.empty() bool si esta vacia

def cola_random(n:int,desde:int,hasta:int)->Pila:
    c:Cola = Cola()
    lista_num_random:list[int] = generarNrosAlAzar(n,desde,hasta)
    for i in lista_num_random:
        c.put(i)
    return c

#ejercicio 14
def cantidadElementos(c:Cola)->int:
    c_aux:Cola=Cola()
    count:int=0
    while not c.empty():
        elem=c.get()
        count += 1
        c_aux.put(elem)
    while not c_aux.empty():
        elem=c_aux.get()
        c.put(elem)
    return count
#print(cantidadElementos(cola_random(10,0,11)))

#ejercicio 15
def cola_a_lista(c:Cola)->list:
    l:list=[]
    c_aux:Cola = Cola()
    while not c.empty():
        elem=c.get()
        l.append(elem)
        c_aux.put(elem)
    while not c_aux.empty():
        elem = c_aux.get()
        c.put(elem)
    return l

def buscarElMaximoEnLaCola(c:Cola)->int:
    lista:list=pila_da_lista(c)
    res:int=max(lista)
    return res

#ejercicio 16
def armarSecuenciaDeBingo()->Cola[int]:
    c:Cola=cola_random(12,0,100)
    return c
def armarBolillero()->Cola[int]:
    c:Cola=cola_random(random.randint(0,100),0,100)
    return c

def jugarCartonDeBingo(carton:list[int],bolillero:Cola[int])->int:
    puntos:int=0
    bolillero_aux:Cola=Cola()
    while not bolillero.empty():
        elem = bolillero.get()
        bolillero_aux.put(elem)
        for i in carton:
            if i == elem:
                puntos += 1

    while not bolillero_aux.empty():
        elem=bolillero_aux.get()
        bolillero.put(elem)
    puntos_faltantes:int= 12-puntos
    return puntos_faltantes

#carton:Cola = armarSecuenciaDeBingo()
#bolillero:Cola = armarBolillero()

#print(cola_a_lista(carton))
#print(cola_a_lista(bolillero))
#print(jugarCartonDeBingo(cola_a_lista(carton),bolillero))

#ejercicio17    
def nPacientesUrgentes(c:Cola[(int,str,str)])->int:
    c_aux:Cola=Cola()
    count:int=0
    while not c.empty():
        elem = c.get()
        c_aux.put(elem)
        if elem[0] in range(1,4):
            count += 1
    while not c_aux.empty():
        elem=c_aux.get()
        c.put(elem)
    return count

#cola = Cola()
#cola.put((1, "Juan", "Cardiologia"))
#cola.put((2, "Maria", "Pediatria"))
#cola.put((3, "Carlos", "Oftalmologia"))
#cola.put((4, "Ana", "Dermatologia"))
#cola.put((1, "Pedro", "Neurologia"))

#print(nPacientesUrgentes(cola))  # Salida esperada: 4


#DICCCIONARIOS
#ejercicio 18

def agruparPorLongitud(nombre_archivo:str)->dict:
    ruta_archivo:str=crear_ruta(addtxt(nombre_archivo))
    archivo:str = open(ruta_archivo,'r')
    diccionario:dict={}
    for linea in archivo:
        palabras = linea.split() #divide la linea en palabras
        for palabra in palabras:
            if len(palabra) in diccionario:
                diccionario[len(palabra)]+= 1
            else:
                diccionario[len(palabra)]= 1
    archivo.close()
    return diccionario


#print(agruparPorLongitud("test"))

#ejercicio 19

def diccionarioNotas()->dict:
    archivo:str = open("nombre_archivo.csv", "r")
    diccionario:dict = {}
    for linea in archivo.readlines():
        campos = linea.split(",")
        lu=campos[0]
        diccionario[campos[0]]=promedioEstudiante(campos[0])
    archivo.close()
    return diccionario

#ejercicio20
def laPalabraMasFrecuente(nombre_archivo:str)->str:
    ruta_archivo:str=crear_ruta(addtxt(nombre_archivo))
    archivo:str = open(ruta_archivo,'r')
    diccionario:dict={}
    for linea in archivo:
        palabras =linea.split()
        for palabra in palabras:
            if palabra in diccionario:
                diccionario[palabra]+=1
            else:
                diccionario[palabra]=1
    archivo.close()
    claves:list=diccionario.keys()
    valores:list=list(diccionario.items())
    indice:int=indiceDelMaximo(valores)
    res=claves[indice]
    return res

def indiceDelMaximo(l: list) -> int:
    if len(l) == 0:
        return -1  # Manejar el caso de una lista vacia

    max_index = 0
    for i in range(1, len(l)):
        if l[i] > l[max_index]:
            max_index = i

    return max_index
