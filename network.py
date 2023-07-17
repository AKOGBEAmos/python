def net_address(addr1, addr2, m):
    try:
        address1 = addr1.split('.')
        address2 = addr2.split('.')
    except:
        return -1

    address1 = [int(x) for x in address1]
    address2 = [int(x) for x in address2]
    
    i = 0
    j = 0
    
    while i <= 3:
        a, b = bin(address1[i]), bin(address2[i])
        
        if (int(a, 2) & int(b, 2)) == int(a, 2):
            i += 1
            if (m - j) < 8:
                j += (m - j)
            else:
                j += 8
        else:
            break
    
    if j == m:
        return 1
    else:
        return -1

    

addr1=input("Entrez ladresse dun reseau.\n")
addr2=input("Entrez ladresse de la machine\n")
mask1=int(input("Entrez le masque CIDR de ladresse reseau.\n"))
mask2=int(input("Entrez le masque CIDR de ladresse de la machine.\n"))

if mask1==mask2:
    value=net_address(addr1,addr2,mask1)
    if (value==True):
        print("Cette machine appartient au reseau.\n")
    else:
        print("Cette machine est pas de ce reseau.\n")
else:
    print("Cette machine est pas de ce reseau.\n")

