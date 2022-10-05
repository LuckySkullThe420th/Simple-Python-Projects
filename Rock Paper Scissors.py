import random
#player score
player = 0
#computer score
computer = 0
#dictionary to save the values for input
rock_paper_scissors_list = ["paper", "scissors", "rock", "q"]


    #loops
while True:
    #input
    user_input = int(input("Rock, Paper, or Scissors? (press 3 to quit): "))

    #computer gets a random value
    rand_int = random.randint(0, 2)

    #limiting negative numbers

    if rand_int < 0:
        print("rerolling...")
        print(random.randint(1,2))

    #rock
    if user_input == 2:
        print(" ")
        print("you chose", rock_paper_scissors_list[2], "CPU chooses...")
        print("------------")
        print("CPU:", rand_int)

        if rand_int > user_input:
            computer += 1
            print("Computer wins!")
            print("Score:",computer)
            print("------------")

        elif rand_int < user_input:
            player += 1
            print("Player wins!")
            print("Score:", player)
            print("------------")
    #paper
    if user_input == 0:
        print(" ")
        print("you chose", rock_paper_scissors_list[0],"CPU chooses...")
        print("------------")
        print("CPU:", rand_int)   
        print("------------")


        if rand_int > user_input:
            computer += 1
            print("Computer wins!")
            print("Score:", computer)
            print("------------")
        elif rand_int < user_input:
            player += 1
            print("Player wins!")
            print("Score:", player)
            print("------------") #12 lines
    #scissors
    if user_input == 1:
        print("------------")
        print("you chose", rock_paper_scissors_list[1], "CPU chooses...")
        print("------------")
        print("CPU:", rand_int)   
        print("------------")

        if rand_int > user_input:
            computer += 1
            print("Computer wins!")
            print("Score:", computer)
            print("------------")

        elif rand_int < user_input:
            player += 1
            print("Player wins!")
            print("Score:", player)
            print("------------")


    #final score
        final_score = (f"player's score {player} - CPU's score {computer}") 
        if player >= 3:
            if player > computer:
                print(final_score)
                print("Congrats! Player wins!")
                break
        elif computer >= 3:
            if player < computer:
                print(final_score)
                print("The CPU has defeated you...try again next time.")
                break    

    #quit
    if user_input == 3:
        break
    #for random inputs
    if user_input not in {"rock", "paper", "scissors"}:
        continue

  