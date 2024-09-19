import random
options = (['rock', 'paper', 'siccers'])
computer_ch = random.choice(['rock', 'paper', 'siccers'])
print(computer_ch)

def mesage(texto):
    print (f"********** {texto}. *****")

def game():
    while True :
        user_ch= input("choose a world of this list : 'rock', 'paper', 'siccers': ")
        
        if user_ch == "quit":
            break

        if user_ch not in options:
            mesage("Not allow")
            continue

        if user_ch == computer_ch:
            mesage("tie")
    
        elif (user_ch == "rock" and computer_ch == "scissors") or (user_ch == "paper" and computer_ch == "rock") or (user_ch == "scissors" and computer_ch == "paper"):
            mesage("Won")

        else:
            mesage(" you lose")

game()