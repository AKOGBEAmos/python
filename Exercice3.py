def average(list):
    total=0
    for i in list:
        total+=i
    avg=total/12
    return avg
BEN=[2.67, 1.00, 1.21, 3.09, 3.43, 4.71, 3.88, 3.08, 4.10, 2.62, 1.01, 5.93]
TOG=[6.83, 3.63, 7.20, 2.68, 2.05, 2.96, 1.04, 0.00, 0.03, 6.71, 8.28, 6.85]
avg1=average(BEN)
avg2=average(TOG)
num1=0
num2=0
for i in BEN:
    if i>avg1:
        num1+=1
for i in TOG:
    if i>avg1:
        num2+=1
mois=['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']
month=[]
j=0
for i in range(0,12):
    if BEN[i]<TOG[i]:
        j+=1
        month.append(mois[i])
print("La moyenne des précipitations mensuelles au Bénin est de {};celle au Togo est de {}\nIl y a au Bénin {} mois où la précipitation est supérieure à la moyenne et au Togo,{}\n".format(avg1,avg2,num1,num2))
print(f"Il y a en tout {j} mois qui sont:\n")
for i in month:
    print("\n",i)



