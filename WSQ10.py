# WSQ
#Oscar Eduardo Sanchez 

import math

def suma(L):
	s= sum(L)
	return s
def standard (L):
	s= suma(L)
	r= math.sqrt(s)
	return r
def average(L):
	a= suma(L)/10.0
	return a

a=float(input("Dame el primer numero: "))
b=float(input("Dame el segundo numero: "))
c=float(input("Dame el tercer numero: "))
d=float(input("Dame el cuarto numero: "))
e=float(input("Dame el quinto numero: "))
f=float(input("Dame el sexto numero: "))
g=float(input("Dame el septimo numero: "))
h=float(input("Dame el octavo numero: "))
i=float(input("Dame el noveno numero: "))
j=float(input("Dame el decimo numero: "))

L=[]
L.append(a)
L.append(b)
L.append(c)
L.append(d)
L.append(e)
L.append(f)
L.append(g)
L.append(h)
L.append(i)
L.append(j)

x=suma(L)
y=average(L)
z=standard(L)
print("La suma de los numeros en la lista es: ", x)
print("El promedio de los numeros en la lista es: ", y)
print("La raiz cuadrada de los numeros de la lista es: ", z)
