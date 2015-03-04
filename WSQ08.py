# WSQ
#Oscar Eduardo Sánchez
def sum(x,y):
	suma = x+y 
	return suma
def difference(x,y):
	resta = x-y
	return resta
def product(x,y):
	multi = x*y
	return multi
def division(x,y):
	div = x//y
	return div
def remainder(x,y):
	resdiv = x%y
	return resdiv
x = int(input("Dame un número: "))
y = int(input("Dame otro número: "))
a = sum(x,y)
b = difference(x,y)
c = product(x,y)
d = division(x,y)
e = remainder(x,y)
print("La suma de los numeros es: ", a)
print("La resta de los numeros es: ", b)
print("La multiplicacion de los numeros es: ", c)
print("La division de los numeros es: ", d)
print("El residuo de los numeros es: ", e) 
