from Conversion import *
n="Menu de conversion en base"
n=n.center(25,'-')
print(n)
print("1-Conversion de la base 10 en binaire\n2-Conversion du binaire en base 10\n3-Conversion de la base 10 en base octal")
print("4-Conversion de la base octal en base 10\n5-Conversion de la base 10 en hexadécimal\n6-Conversion de l'hexadécimale en base 10\n0-Quitter le menu\n")
c=int(input("Veuillez choisir une option de conversion\n"))
while c!=0:
    if c==1:
        x=int(input("Entrer le nombre à convertir en binaire\n"))
        print("Le nombre {} est égal à {} en binaire.\n".format(x,déci_bin(x)))
        break
    elif c==2:
        x=(input("Entrez le nombre que vous voulez convertir en base 10\n"))
        print("Le nombre {} est égal à {} en base 10.\n".format(x,bin_déci(x)))
        break
    elif c==3:
        x=(input("Entrez le nombre que vous voulez convertir en base 8\n"))
        print("Le nombre {} est égal à {} en base 8.\n".format(x,déci_octa(x)))
        break
    elif c==4:
        x=(input("Entrez le nombre que vous voulez convertir en base 10\n"))
        print("Le nombre {} est égal à {} en base 10.\n".format(x,octa_déci(x)))
        break
    elif c==5:
        x=(input("Entrez le nombre que vous voulez convertir en hexadécimale\n"))
        print("Le nombre {} est égal à {} en base 10.\n".format(x,déci_hex(x)))
        break
    elif c==6:
        x=(input("Entrez le nombre que vous voulez convertir en base 10\né"))
        print("Le nombre {} est égal à {} en base 10.\n".format(x,hex_déci(x)))
        break
    else:
        print("Unfind option !!Veuillez réessayer.\n")
        c=int(input("Veuillez choisir une option de conversion\n"))
        break