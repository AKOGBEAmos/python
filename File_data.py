import os

def comptage(in_filename, out_filename,path):
    if os.path.isfile(os.path.join(path, in_filename))==True:
        try:
           with open(os.path.join(path, in_filename), "r", encoding='utf-8') as file:
               lines=0
    
               for line in file:
                   lines+=1
                   words=0
                   char=0
                   word=line.split(' ')
                   words+=len(word)
                   for x in word:
                       c=0
                       for character in x:
                           c+=1
                       char+=c
                   with open(os.path.join(path,out_filename),'a', encoding='utf-8') as properties:
                       properties.write(f"{lines} {words} {char}\n")
                       properties.write(f"{line}\n")
           return 1
        except:
            return -1
    else:
        return -1


filename=input("Entrez le nom du fichier dont vous voulez les propriétés.\n")
chemin=input("Donnez le chemin absolu vers ce fichier\n")
output=input("Entrez le nom du fichier de destination des propriétés.\n")
data=comptage(filename,output,chemin)
if data==1:
    out_filepath = os.path.join(chemin,output)
    print(f"Les données sur le fichier {filename} sont ici: {out_filepath}")
else:
    print("Il ya une erreur sur le fichier.\n")