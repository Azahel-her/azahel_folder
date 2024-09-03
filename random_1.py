import random
my_word = random.choice(['python', 'java', 'javascript', 'ruby', 'html', 'css'])
print (my_word)
while True :
    word= input("choose a world of this list : 'python', 'java', 'javascript', 'ruby', 'html', 'css' : ")
    if (word) == "quit":
        break
    else :
        if(word)==my_word:
            print("you guessed the correct one")
        elif(word) ==("choose a word:'python', 'java', 'javascript', 'ruby', 'html', 'css'") :
            print("")
        else :
            print("that is not the correct word")
        
        
        
    
