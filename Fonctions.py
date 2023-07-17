from math import* 

def factoriel(n):
    if(n==0 or n==1):
        return n
    else:
        return n*factoriel(n-1)

def puissance(n, m):
    p=1
    for i in range (m+1):
        p*=n
    return p

def surface(c):
    return c*c

def area(r):
    return r*r*pi

print("*****Menu de fonctions*****\n1-Factoriel\n2-Puissance dun nombre\n3-Surface d'un carre\n4- Aire dun cercle\n5-Quitter\n")
c=int(input("Veuillez choisir une option.\n"))
while (c!=5):
    if c==1:
        nombre=int(input("Entrez le nombre dont vous voulez le factoriel\n"))
        print("{}!={}\n".format(nombre, factoriel(nombre)))
    elif c==2:
        nombre=int(input("Entrez la base de la puissance\n"))
        m=int(input("Entrez lexposant\n"))
        print("{}^{}={}\n".format(nombre, m, puissance(nombre,m)))
    elif c==3:
        cote=int(input("Entrez la longueur du cote\n"))
        print("La surface de ce carre est {}\n".format(surface(cote)))
    elif c==4:
        rayon=int(input("Entrez le rayon du cercle.\n"))
        print("Ce cercle a une aire de: {}\n".format(area(rayon)))
    else:
        print("Option invalide\nVeuillez reessayer.")
    
    print("*****Menu de fonctions*****\n1-Factoriel\n2-Puissance dun nombre\n3-Surface d'un carre\n4- Aire dun cercle\n5-Quitter\n")
    c=int(input("Veuillez choisir une option.\n"))

