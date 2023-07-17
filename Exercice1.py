def position(numbre):
    for i in nombre:
        if mini in i:
            c=i.index(mini)
            l=nombre.index(i)
    return (l,c)
nombre=[]
column=[]
sm=0
spos=0
sneg=0
index=0
for  i in range(0,3):
    for j in range(0,2):
        a=int(input("Elément du tableau"))
        sm+=a
        column.append(a)
        if a>=0:
            spos+=a
            index+=1
        else:
            sneg+=a
        print(sneg)
    nombre.append(column)
"""maxi = (max(max(i)for i in nombre))
mini = (min(min(i)for i in nombre))
print("La somme totale des élément est:{},celle des nombres positifs:{} et celle des négatifs est:{}\n".format(sum,spos,sneg))
print(f"le maximum est {maxi} \n Le minimum est {mini} \n l'index du minimum est:{position(numbre)}")"""
