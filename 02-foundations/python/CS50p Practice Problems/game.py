import random

def main(level, randint):
    # ensure user's range fits reqs
    while True:
        if level > 0:
            break
        else:
            level = int(input("Level: "))

    # user's guess
    while True:
        try:
            guess = int(input("Guess: "))
            break
        except ValueError:
            None

    # check
    if guess <= 0:
        main(level, randint)
    elif guess == randint:
        print("Just right!")
        raise SystemExit
    elif guess < randint:
        print("Too small!")
        print()
        main(level, randint)
    elif guess > randint:
        print("Too large!")
        print()
        main(level, randint)


level = int(input("Level: "))
randint = random.randint(1, level)
main(level, randint)
