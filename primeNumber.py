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
