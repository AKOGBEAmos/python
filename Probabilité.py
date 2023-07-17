def factoriel(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factoriel(n-1)
def arrangement(n,p):
    return int(factoriel(n)/factoriel(n-p))
def combinaison(n,p):
    return int(arrangement(n,p)/factoriel(p))

n="Menu"
n=n.center(20,'*')
print(n)
print("1-Calculer le factoriel d'un nombre\n2-Calculer l'arrangement de p dans n\n3-Calculer la combinaison de p dans n\n4-Générer le triangle de Pascal\n")
print("0-Quitter le menu\n")
x=int(input("Enter the option of your probability operation.\n"))
while x!=0:
    if x==1:
        m=int(input("Entrez au clavier le nombre.\n"))
        print("{}!={}".format(m,factoriel(m)))
        break
    elif x==2:
        m=int(input("Entrez au clavier la base de l'opérande(n).\n"))
        p=int(input("Entrez au clavier le nombre.\n"))
        print("{}P{}={}".format(p,m,arrangement(m,p)))
        break
    elif x==3:
        m=int(input("Entrez au clavier la base de l'opérande(n).\n"))
        p=int(input("Entrez au clavier le nombre.\n"))
        print("{}C{}={}".format(p,m,combinaison(m,p)))
        break
    elif x==4:
        m=int(input("Entrez au clavier l'ordre du triangle de Pascal.\n"))
        break
    else:
        print("Option invalide.\nVeuillez réessayer.\n")

