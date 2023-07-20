import random
CODE_LENGTH = 4
COLORS = ["B", "Y", "R", "G", "P", "W"]
TRIES = 10
PRIZE = 110


def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code


def user_code():
    while True:
        guess = input("Guess: ").upper().split(" ")
        if len(guess) != CODE_LENGTH:
            print(f"Please write {CODE_LENGTH} colors.")
            continue
        for color in guess:
            if color not in COLORS:
                print("Please enter valid colors")
                break
        else:
            break
    return guess


def check_code(guess_code, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0
    correct_colors = set()

    for i, (guess, real) in enumerate(zip(guess_code, real_code)):
        if guess == real:
            correct_pos += 1
            correct_colors.add(i)
        else:
            if real in color_counts:
                color_counts[real] += 1
            else:
                color_counts[real] = 1

    for i, guess in enumerate(guess_code):
        if i in correct_colors:
            continue
        if guess in color_counts and color_counts[guess] > 0:
            incorrect_pos += 1
            color_counts[guess] -= 1

    return correct_pos, incorrect_pos


def game():
    real = generate_code()
    print("Write 4 colors separated by spaces, to guess the code.")
    print("Colors are:", *COLORS, ". " f"You have {TRIES} tries.")
    print("The initial prize is $100, after every try prize will decrease by $10.")
    for attempt in range(1, TRIES + 1):
        guess = user_code()
        correct, incorrect = check_code(guess, real)
        if correct == CODE_LENGTH:
            current_prize = PRIZE - 10 * attempt
            print(f"You won in {attempt} tries and you deserve ${current_prize}.")
            break
        print(f"Correct position: {correct}, incorrect: {incorrect}")
        if attempt == 10:
            print("You lose, code was:", *real)


game()