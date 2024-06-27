from project import Letter, check_green, check_yellow, valid_word


def test_check_green_no_match():

    answer = 'HELLO'
    guess = 'CRAZY'
    clue_list = [Letter('#') for _ in range(5)]
    guess_list = [Letter(i) for i in guess]
    answer_list = [Letter(i) for i in answer]
    check_green(clue_list, guess_list, answer_list)

    for i in range(5):
        assert clue_list[i].color == ''


def test_check_green_one_match():
    answer = 'HELLO'
    guess = 'LEVEL'
    clue_list = [Letter('#') for _ in range(5)]
    guess_list = [Letter(i) for i in guess]
    answer_list = [Letter(i) for i in answer]
    check_green(clue_list, guess_list, answer_list)

    assert clue_list[0].color == ''
    assert clue_list[1].color == 'green'
    assert clue_list[2].color == ''
    assert clue_list[3].color == ''
    assert clue_list[4].color == ''

def test_check_green_all_match():
    answer = 'TIMER'
    guess = 'TIMER'
    clue_list = [Letter('#') for _ in range(5)]
    guess_list = [Letter(i) for i in guess]
    answer_list = [Letter(i) for i in answer]
    check_green(clue_list, guess_list, answer_list)

    assert clue_list[0].color == 'green'
    assert clue_list[1].color == 'green'
    assert clue_list[2].color == 'green'
    assert clue_list[3].color == 'green'
    assert clue_list[4].color == 'green'

def test_check_yellow_no_match():
    answer = 'HELLO'
    guess = 'CRAZY'
    clue_list = [Letter('#') for _ in range(5)]
    guess_list = [Letter(i) for i in guess]
    answer_list = [Letter(i) for i in answer]
    check_yellow(clue_list, guess_list, answer_list)

    for i in range(5):
        assert clue_list[i].color == ''

def test_check_yellow_some_match():
    answer = 'HELLO'
    guess = 'SHAIL'
    clue_list = [Letter('#') for _ in range(5)]
    guess_list = [Letter(i) for i in guess]
    answer_list = [Letter(i) for i in answer]
    check_yellow(clue_list, guess_list, answer_list)

    assert clue_list[0].color == ''
    assert clue_list[1].color == 'yellow'
    assert clue_list[2].color == ''
    assert clue_list[3].color == ''
    assert clue_list[4].color == 'yellow'

def test_check_yellow_with_green():
    answer = 'HELLO'
    guess = 'LEVEL'
    clue_list = [Letter('#') for _ in range(5)]
    guess_list = [Letter(i) for i in guess]
    answer_list = [Letter(i) for i in answer]
    check_green(clue_list, guess_list, answer_list)
    check_yellow(clue_list, guess_list, answer_list)

    assert clue_list[0].color == 'yellow'
    assert clue_list[1].color == 'green'
    assert clue_list[2].color == ''
    assert clue_list[3].color == ''
    assert clue_list[4].color == 'yellow'

def test_valid_guess():
    guess = 'TIMER'
    assert valid_word(guess) == True

def test_invalid_guess():
    guess = 'TIMEH'
    assert valid_word(guess) == False

