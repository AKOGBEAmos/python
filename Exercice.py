from math import sqrt

def listElement(list):
    for element in list:
        print(element)

def sumListe(liste):
    sum=0
    """
    On initialise une variable somme des éléments à  0 
    et on y ajoute chaque élément présent dans la liste    
    """
    for element in liste:
        sum+=element
    return sum

def conversionFarhenheit(temperature):
    #(0 °C × 9/5) + 32 = 32 °F

    t=(temperature*9/5)+32
    return t

def conversionCelcius(temperature):
    #Par analogie, 1°C=(t(°F)-32)*5/9
    t=(temperature-32)*5/9
    return t

def evenNumbers(number):
    """
    Un nombre pair est un nombre qui est divisible par 2
    """
    for i in range(number):
        if(i%2==0):  #On vérifie la valeur du modulo de chaque nombre inférieur à notre borne
            print(i)

#fonction de détermination d'un nombre premier.
def is_prime(number):
    """Un nombre premier n'a que deux diviseurs 1 et lui même.
        Donc il ne devrait avoir qu'un seul diviseur qui lui est inférieur."""
    prime=0
    for i in range(1,number):
        if (prime>1):
            break
        elif(number%i==0):
            prime+=1
    if(prime==1):
        return True 
    else:
        return False


def prime(number):
    if (number==1 or number<0):
        return False
    elif (number==2):
        return True
    else:
        num=int(sqrt(number))
        i=3
        while(i<=num):
            if (number%i==0):
                return False
            i+=2
        return True

n=1000001
print(prime(n))

    
def dictionnary(dico):
    for element in dico.values():
        #La méthode dico.values()retourne les valeurs contenues dans le dictionnaire.
        print (element)

def fibonacci(number):
    if (number==0 or number==1):
        return(1)
    else:
        return fibonacci(number-1)+fibonacci(number-2)

#Le code pour compléter la fonction
"""
n=int(input("Entrez la valeur maximum du terme de la suite de Fibonacci\n"))
i=0
while(fibonacci(i)<n):
    print(fibonacci(i)) 
    i+=1   
"""

def voyelles(word):
    liste=['a','e','i','o','u','y']#Ceci est la liste des voyelles
    for letter in word:
#On parcourt chaque lettre du mot et on vérifie s'il est présent dans la liste 
        if letter in liste:
            print(letter)

def odd_numbers(liste):
    for number in liste:
        if (i%2!=0):
            print (number)

def characters(liste):
    if(type(liste)==list):
        i=0
        # Parcours de la liste caractère par caractère
        for char in liste:
            i+=1
        return i

def reverselist(liste):
    reverse=[]
    reverse.append(liste[len(liste)-1])
    i=2
    while(i<=len(liste)):
        reverse.append(liste[len(liste)-i])
        i+=1
    return reverse

def factoriel(num):
    """On utilisera les fonctions récursives pour trouver le factoriel
       en utilisant la formule fact(n)=n*n-1*...*2*1
    """
    if (num==0 or num==1):
        return 1
    else:
        return num*factoriel(num-1)

def palindrome(word):
    """
        Un mot palindrome est un mot identique lorsqu'il est inversé.
        ex: Bob,elle
    """
    reverse=[]
    reverse=reversed(word)
    if word==reverse:
        return True
    else:
        return False
    
def customCamelCase(word):
    camelWord=[]
    if (word[0].isupper()==True):
        for i in range(len(word)):
            if (i%2==0):
                camelWord.append(word[i].upper())
            else:
                camelWord.append(word[i])
    else:
        for i in range(len(word)):
            if (i%2!=0):
                camelWord.append(word[i].upper())
            else:
                camelWord.append(word[i])
    return camelWord




        



    
