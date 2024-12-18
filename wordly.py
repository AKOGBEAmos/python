#Mad Lib games

story_length = int(input("Enter the number of sentences you want fo the story.\n"))
while story_length <=1 or story_length >5:
    print("Your story must not be too short nor too long.")
    story_length = int(input("Enter the number of sentences you want fo the story.\n"))

mad_libs_words = []
if story_length %2 !=0:
    match story_length:
        case 3:
            for x in range(3):
                word = input("Enter the word n°{} ".format(x))
                mad_libs_words.append(word)
            print("This story is no re@l fun.")
            #Outcome
            print("On a beautiful {} day, I went to the zoo. I saw a funny {} monkey swinging from the trees. Then, I spotted a majestic {} lion lounging in the sun.".format(mad_libs_words[2], mad_libs_words[1], mad_libs_words[0]))
        case 5:
            for x in range(5):
                word = input("Enter the word n°{} ".format(x))
                mad_libs_words.append(word)
            print("This story is no re@l fun.")
            #Outcome
            print("On a beautiful {} day, I went to the zoo. I saw a funny {} monkey swinging from the trees. Then, I spotted a majestic {} lion lounging in the sun.  What a wild and {} experience! Next time Central {} will be crowded".format(mad_libs_words[2], mad_libs_words[4], mad_libs_words[0], mad_libs_words[3], mad_libs_words[1]))
else:
    match story_length:
        case 2:
            for x in range(2):
                word = input("Enter the word n°{} ".format(x))
                mad_libs_words.append(word)
            print("This story is no re@l fun.")
            #Outcome
            print("I saw a funny {} monkey swinging from the trees. It was a beautiful {} day, when I went to the zoo. ".format(mad_libs_words[1], mad_libs_words[0]))
        case 4:
            for x in range(4):
                word = input("Enter the word n°{} ".format(x))
                mad_libs_words.append(word)
            print("This story is no re@l fun.")
            #outcome
            print("I saw a funny {} monkey swinging from the trees. It was a beautiful {} day, when I went to the zoo. What a wild and {} experience! Next time Central {} will be crowded".format(mad_libs_words[0], mad_libs_words[1], mad_libs_words[2], mad_libs_words[3]))