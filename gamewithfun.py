import random
options = (['rock', 'paper', 'Scissors'])
computer_ch = random.choice(['rock' , 'paper'  , 'Scissors' ])
print(computer_ch)

def mesage(texto):
    print (f"********** {texto}. *****")

def numbers():
    "Rock" = int(1)
    "Paper" = int(2)
    "Scissors"=int(3)

def game():
    while True :
        user_ch= input("choose a world of this list : 'rock', 'paper', 'Scissors': ")
        
        if user_ch == "quit":
            break

        if user_ch not in options:
            mesage("Not allow")
            continue

        if user_ch == computer_ch:
            mesage("tie")
    
        elif (user_ch == "rock" and computer_ch == "Scissors" ) or (user_ch == "paper" and computer_ch == "rock" ) or (user_ch == "Scissors" and computer_ch == "paper"  ):
            mesage("Won")

        else:
            mesage(" you lose")


numbers()
game()