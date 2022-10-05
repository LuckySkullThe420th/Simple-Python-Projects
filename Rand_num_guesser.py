import random

#inputs for range
inp = (input("Enter the start of the range: "))
inp2 = (input("Enter the end of the range: "))
#String to int conversion: Input 1
if  inp.isdigit():
     inp = int(inp)
#String to int conversion: Input 2
if inp2.isdigit():
    inp2 = int(inp2)    
#conditionals to check to make sure there are no errors
if inp or inp2 <= 0: 
     print("Please enter a valid integer.")   
     quit()
elif not  inp.isdigit() or inp2.isdigit():
     print("Please enter a valid integer.") 
     quit()
#Num_ of_ attempts      
attempts = 0
#Loop for program
while True:
    #incrementing/keeping check of  attempts
    attempts+=1
    #random int
    rand_int = random.randint(inp, inp2)
    #input for your guess at num
    Guess = (input("Guess a number: "))
    #String to int conversion: Guessing number
    if Guess.isdigit():
        Guess = int(Guess)
        #Conditional in case there was an error
    else:
        print("Please type a valid integer.")
    #If correct, you win! Then a return of attempts will be seen by the player.
    if Guess == rand_int:
        print(f"You guessed the number in {attempts} attempts.")    
        break
       #Program will break after final win.


   
    
    