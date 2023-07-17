"""+===============================================================+
   |n=int(input("Enter the number of blocks of your pyramid\n"))
   |j=1
   |i=n
   |while i>1:
   |i-=1
   |j+=1
   |print("For {} blocks your pyramid's height is {}.\n".format(n,j))


school_class = {}

while True:
    name = input("Enter the student's name: ")
    if name == '':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    if score not in range(0, 11):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)"""
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)














