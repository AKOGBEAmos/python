def pgcd(number1,number2):
    #On vérifie que la division est possible en faisant une comparaison i.e il faut que number1>number2)
    if number1<number2:
        var=number1
        number1=number2
        number2=var
    elif number1==0:
        """Si number1 est nul alors directement le pgcd=number2 
            car, O est multiple de tous les nombres."""
        return number2
        #On utilise l'algorithme d'Euclide
    r=number1%number2
    while(r!=0):
        number1=number2
        number2=r
        r=number1%number2
    return number2
    
//Juste un code pour tester la fonction.

a=int(input("Entrez le premier nombre.\n"))
b=int(input("Entrez le deuxième nombre.\n"))
print(f"Le PGCD de({a},{b}) est: {pgcd(a,b)}")
