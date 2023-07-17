
hour=int(input("Donnez l'heure de début de la réunion.\n"))
minute=int(input("Donnez la minute exacte.\n"))
duration=int(input("Quelle est la durée de l'évènement en minutes?\n"))
jour=0
if hour+duration//60>24:
    jour+=(duration//60)//24
    hour=duration//60-24
tmp=minute+duration%60
if tmp>60:
    hour+=1
    minute+=duration-60
if jour==0:
    print(f"L'heure de  fin de l'évènement est:\n{hour}h:{minute}min.")
elif jour==1:
    print(f"L'heure de  fin de l'évènement est:\n{hour}h:{minute}min le lendemain.")
else:
    print(f"L'heure de  fin de l'évènement est à:\n{hour}h:{minute}min dans{jour}jours.")