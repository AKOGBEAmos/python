from arithmetic import operation

print ("Operation with a and b ")
a = int(input(" Enter number a: "))
b = int(input(" Enter number b: "))

#Print the multiplication and the gcd of a and b
multiplicate = operation.multiplication(a,b)
gcd = operation.pgcd(a,b)
print(f" {a}*{b}= {multiplicate} ")
print(f"The GCD (Great Common Divisor) of {a} and {b} is: {gcd}")