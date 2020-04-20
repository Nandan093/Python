import random
attempts = int(input("Enter the attempts : ")) # Asking number of attempts from the user
counter_A, counter_computer, counter_tied= 0 , 0 , 0 # Initializing the counters
i = 0 #initializing thr counter for while loop

while i < attempts:
    
    #No. of attempts
    print("Attempt = ",i + 1 )

    #Accepting choices from player
    player = input("Player choice [Snake/Water/Gun] : ")

    #Choosing elements randomly by using random module
    choices = ['Snake', 'Water', 'Gun']
    computer = random.choice(choices)

    #Output the Computer choices
    print("Computer choice : ",computer)

    #Comparing each choice of player with available choices(Snake/Water/Gun)
    if(player == "Snake"):
        if(computer == "Water"):
            print("Player has won this attempt")
            counter_A = counter_A + 1
        elif(computer == "Gun"):
            print("Computer has won this attempt")
            counter_computer = counter_computer + 1
        elif(computer == "Snake"):
            print("Match is tied")
            counter_tied = counter_tied + 1
    elif(player == "Water"):
        if(computer == "Gun"):
            print("Player has won this attempt")
            counter_A = counter_A + 1
        elif(computer == "Snake"):
            print("Computer has won this attempt")
            counter_computer = counter_computer + 1
        elif(computer == "Water"):
            print("Match is tied")
            counter_tied = counter_tied + 1
    elif(player == "Gun"):
        if(computer == "Snake"):
            print("Player has won this attempt")
            counter_A = counter_A + 1
        elif(computer == "Water"):
            print("Computer has won this attempt")
            counter_computer = counter_computer + 1
        elif(computer == "Gun"):
            print("Match is tied")
            counter_tied = counter_tied + 1
    #Incrementing the counter
    i = i + 1
#Showing result to the user
print("Total number of attempts = ",attempts)
print("No. of attempts player wins = ",counter_A)
print("No. of attempts computer wins = ",counter_computer)
print("No of attempts tied = ",counter_tied)

'''
Output:-
Enter the attempts : 5
Attempt =  1
Player choice [Snake/Water/Gun] : Gun
Computer choice :  Water
Computer has won this attempt
Attempt =  2
Player choice [Snake/Water/Gun] : Water
Computer choice :  Water
Match is tied
Attempt =  3
Player choice [Snake/Water/Gun] : Snake
Computer choice :  Gun
Computer has won this attempt
Attempt =  4
Player choice [Snake/Water/Gun] : Gun
Computer choice :  Gun
Match is tied
Attempt =  5
Player choice [Snake/Water/Gun] : Gun
Computer choice :  Water
Computer has won this attempt
Total number of attempts =  5
No. of attempts player wins =  0
No. of attempts computer wins =  3
No of attempts tied =  2
'''
