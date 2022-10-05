magic_number = 10

while True:
    guess = int(input("Guess my number: "))
    if guess == magic_number:
        print("You got it!")
        break
    print("Try again!")
