import random

def guess_the_number(x):

    print("================================")
    print(" Welcome to the game! ")
    print("================================")
    print("guess the number generated for the computer.")

    random_num = random.randint(1, x)
    prediction = 0

    while prediction != random_num:
        prediction = int(input(f"Guess the number between 1 y {x}: "))

        if prediction < random_num:
            print("try again. this number is to low.")
        elif prediction > random_num:
            print("try again. this number is to high.")

    print(f"Congratulations, you guessed the number {random_num} correctly")

guess_the_number(10)