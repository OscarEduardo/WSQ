# Quiz
#Oscar Eduardo Sanchez
import statistics

def leernumero(a):
    x=open(a,"r")
    y=0
    L=0
    lista=[]
    for i in x:
        y=y+int(i)
        L=L+1
        lista.append(int(i))
    r=statistics.stdev(lista)
    print("El total de los valores son:",y)
    print("El numero de valores son:",L)
    print("La medida aritmetica de los valores es:",(y/L))
    print("La division es:", r)

leernumero("numeros.txt")
