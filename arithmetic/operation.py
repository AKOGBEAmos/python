from math import *

# Arithmetic and basic calculaions

def add(a, b):
    return (a + b)

def substract(a,b):
    return ( a - b)

def multiplication(a,b):
    return (a * b)

def division(a,b):
    try:
        return(a / b)
    #Managing ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"Sorry you enter 0 as value for b that causes the {e}")

def modulo(a,b):
    try:
        return(a % b)
    #Managing ZeroDivisionError
    except ZeroDivisionError as e:
        print(f"Sorry you enter 0 as value for b that causes the {e}")

def factorial(a):
    fact_a = 1
    for i in range(2,a+1):
        fact_a *= i
    return (fact_a)

def arrangement(n,k):
    #The Arrangement operation is done through this formula n! / (n-k)!
    return (factorial(n) / factorial(n-k))

def combination(n,k):
    #The combination operation is done trough this formula n! / k!(n-k)!
    Cnk = factorial(n) / (factorial(k) * factorial(n-k))
    return Cnk

def pgcd(a,b):
    pgcd = 1
    rest = 1
    while (rest !=0):
        rest = a % b
        a = b 
        b = rest
        
    return a


