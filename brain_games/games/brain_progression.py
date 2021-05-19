from random import randint


def show_game_rules():
    """Show game rules."""
    print("What number is missing in the progression?")


def ask_question():
    """Ask question.

    :returns:
        tuple progression, index_of_missing_number
    :rtype
        (range, int)
    """
    max_progression_length = 10
    min_progression_length = 5
    progression_length = randint(min_progression_length, max_progression_length)
    progression_step = randint(1, 10)
    progression_start = randint(1, 10)
    progression_stop = progression_start + progression_step * progression_length
    progression = range(progression_start, progression_stop + 1, progression_step)
    index_of_missing_number = randint(0, progression_length - 1)
    print('Question:', end=' ')
    for index, number in enumerate(progression):
        if index == index_of_missing_number:
            print('..', end=' ')
            continue
        print(number, end=' ')
    print()
    return progression, index_of_missing_number


def get_correct_answer(question):
    """Get correct answer on question

    :param (range, int) question:
        Question in the form of tuple progression, index_of_missing_number
    :returns:
        Correct answer on question
    :rtype:
        str
    """
    progression, index_of_missing_number = question
    missing_number = tuple(progression)[index_of_missing_number]
    return str(missing_number)
