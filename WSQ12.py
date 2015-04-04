# WSQ
Oscar Sanchez Quintero
x=int(input("Dame un numero: "))
y=int(input("Dame otro numero: "))
def gcd(x,y):
    if(x>y):
        while(x>y):
            x=x-y
            res=x
    elif(x==y):
        res=x
    else:
        while(x<y):
            y==y-x
            res=y
    return res
z=gcd(x,y)
print (z)
