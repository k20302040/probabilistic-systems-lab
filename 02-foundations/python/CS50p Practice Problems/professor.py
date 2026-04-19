import random
import itertools


def main():
    level = get_level()
    ints = generate_integer(level)
    problems = create_problems(ints)


    points = 0
    for item in problems:
        tries = 0
        while tries < 3:
            real_answer = eval(item)
            user_answer = input(item + "= ")

            if int(user_answer) == real_answer:
                points = points + 1
                break
            else:
                print("EEE")
                tries = tries + 1
        else:
            print(f"{item}= {real_answer}")
    print(points)


def create_problems(ints):
    problems = []
    for x , y in itertools.batched(range(20), 2):
        problem = f"{ints[x]} + {ints[y]}"
        problem = problem + " "
        problems.append(problem)
    return problems


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        ints = []
        for _ in range(20):
            ints.append(random.randint(0, 9))
    elif level == 2:
        ints = []
        for _ in range(20):
            ints.append(random.randint(10, 99))
    elif level == 3:
        ints = []
        for _ in range(20):
            ints.append(random.randint(100, 999))
    else:
        main()
    return ints


if __name__ == "__main__":
    main()
