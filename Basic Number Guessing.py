import random
print("Guess the random number from 1-100")
true_value = random.randint(0, 100)

while True:
    guess = input("Enter your guess: ")

    try:
        guess = int(guess)

        if guess == true_value:
            print('You Got It!')
            break
        elif guess > true_value:
            print('Too High')
        else:
            print("Too Low")
    except ValueError:
        print("Enter a valid number")


