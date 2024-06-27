from random import choice


QWERTY = 'Q W E R T Y U I O P\n A S D F G H J K L\n Z X C V B N M'
GREEN = '\033[102m'
YELLOW = '\033[103m'
GREY = '\033[100m'
RESET = '\033[0m'


def main():
    print("Let's play Wordle!")
    answer = pick_answer()
    keyboard_list = [Letter(i) for i in QWERTY]
    turns = 6
    clue_stack = []

    for _ in range(turns):
        while True:
            try:
                guess = input(f"You have {turns} chances to guess the five letter answer: ").upper()
                if len(guess) != 5 or not guess.isalpha() or not valid_word(guess):
                    raise ValueError("Invalid")
                break
            except ValueError as e:
                print(e)

        clue_list = [Letter('#') for _ in range(5)]
        guess_list = [Letter(i) for i in guess]
        answer_list = [Letter(i) for i in answer]

            # check for green clues
        check_green(clue_list, guess_list, answer_list)

            # check for yellow clues
        check_yellow(clue_list, guess_list, answer_list)

            # wrong letters
        for i in range(len(clue_list)):
            if clue_list[i].letter == '#':
                clue_list[i].letter = guess_list[i].letter

            # color qwerty clues
        update_keyboard(keyboard_list, clue_list)


            # print clue_stack with turn number
        print_clue_stack(clue_stack, clue_list)


        for i in range(len(keyboard_list)):
            print(keyboard_list[i].print_color(), end="")
        print()

        if guess == answer:
            print("Success!")
            break

        turns -= 1

    if turns == 0:
        print(f"Failure. The answer was {answer}")


# Randomly select word from answers file
def pick_answer():
    with open('answers.txt', 'r') as file:
        rows = file.readlines()
        answer = choice(rows).strip('\n')
        return answer

# Verify that a guess is in valid list (returns a boolean)
def valid_word(guess):
    with open('valid.txt', 'r') as file:
        rows = [row.strip('\n') for row in file.readlines()]
        return guess in rows


def check_green(clue_list, guess_list, answer_list):
    for i in range(len(answer_list)):
        if answer_list[i].letter == guess_list[i].letter:
            clue_list[i].letter = guess_list[i].letter
            clue_list[i].set_green()
            answer_list[i].set_green()
            guess_list[i].set_green()


def check_yellow(clue_list, guess_list, answer_list):
    for i in range(len(guess_list)):
        for j in range(len(answer_list)):
            if answer_list[j].letter == guess_list[i].letter and answer_list[j].used == False and guess_list[i].color != 'green':
                clue_list[i].letter = guess_list[i].letter
                guess_list[i].set_yellow()
                clue_list[i].set_yellow()
                answer_list[j].set_yellow()
                break


def update_keyboard(keyboard_list, clue_list):
    for i in range(len(keyboard_list)):
        for j in range(len(clue_list)):
            if keyboard_list[i].letter == clue_list[j].letter and clue_list[j].color == 'green':
                keyboard_list[i].set_green()
                break
            elif keyboard_list[i].letter == clue_list[j].letter and clue_list[j].color == 'yellow':
                keyboard_list[i].set_yellow()
                break
            elif keyboard_list[i].letter == clue_list[j].letter:
                keyboard_list[i].set_grey()


def print_clue_stack(clue_stack, clue_list):
    turn_clue = []
    for i in range(len(clue_list)):
        turn_clue.append(clue_list[i].print_color())
    turn_clue = "".join(turn_clue)
    clue_stack.append(turn_clue)
    for i,j in enumerate(clue_stack):
        print(i + 1,j)
    print()


class Letter():
    def __init__(self, letter, color="", used = False):
        self.letter = letter
        self.color = color
        self.used = used

    def set_green(self):
        self.color = 'green'
        self.used = True

    def set_yellow(self):
        self.color = 'yellow'
        self.used = True

    def set_grey(self):
        self.color = 'grey'
        self.used = True

    def print_color(self):
        if self.color == 'green':
            return f"{GREEN}{self.letter}{RESET}"
        elif self.color == 'yellow':
            return f"{YELLOW}{self.letter}{RESET}"
        elif self.color == 'grey':
            return f"{GREY}{self.letter}{RESET}"
        else:
            return self.letter


if __name__ == "__main__":
    main()
