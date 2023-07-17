def puissance(x, n):
    p=1 
    for i in range(0,n):
         p*=x
    return p
def factoriel(n):
    if (n==0 or n==1):
        return 1
    else:
        fac=n*factoriel(n-1)
        return fac

x=int(input("Entrez la valeur de l'exposant du calcul exponentielle.\n"))
n=int(input("Donnez le maximum d'itération pour l'exponentiel.\n"))
expo=0
for i in range(0,n):
    p=puissance(x, i)
    fact=factoriel(i)
    expo+=(p/fact)
print(expo)