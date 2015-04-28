# WSQ
#Oscar Eduardo Sánchez

def check_banana(a):
    x=open(a,'r')
    n=0
    for i in x:
        r=i.lower()
        sub=r.find('banana')
        while sub !=(-1):
            n=n+1
            sub=r.find('banana',(sub+1))
    return(n)

y=check_banana('banana.txt')
print("Este archivo contiene la palabra banana",y,"veces.")
