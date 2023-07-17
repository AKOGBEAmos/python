def déci_bin(i):
    prod=''
    while(i//2!=0):
        j=i%2
        i=i//2
        prod+=str(j)
    prod+=str(i%2)
    prod=''.join(reversed(prod))
    return prod

def bin_déci(i):
    k=''.join(reversed(i))
    j=len(i)-1
    prod=0
    while(j>=0):
        prod+=int(k[j])*2**(j)
        j-=1
    return prod
def déci_octa(i):
    prod=''
    while(i//8!=0):
        j=i%8
        i=i//8
        prod+=str(j)
    prod+=str(i%8)
    prod=''.join(reversed(prod))
    return prod

def octa_déci(i):
    k=''.join(reversed(i))
    j=len(i)-1
    prod=0
    while(j>=0):
        prod+=int(k[j])*8**(j)
        j-=1
    return prod

def equi(i):
    if(i%16)<10:
        return i%16
    else:
        if i%16==10:
            i='A'
        elif i%16==11:
            i='B'
        elif i%16==12:
            i='C'
        elif i%16==13:
            i='D'
        elif i%16==14:
            i='E'
        elif i%16==15:
            i='F'
    return i

def déci_hex(i):
    prod=''
    while(i//16!=0):
        j=equi(i)
        i=i//16
        prod+=str(j)
    prod+=str(equi(i))
    prod=''.join(reversed(prod))
    return prod

def hex_déci(i):
    k=''.join(reversed(i))
    j=len(i)-1
    prod=0
    while(j>=0):
        prod+=int(k[j])*16**(j)
        j-=1
    return prod