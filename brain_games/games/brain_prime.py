from random import randint


def show_game_rules():
    """Show game rules."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def ask_question():
    """Ask question.

    :returns:
        number
    :rtype
        int
    """
    number = randint(0, 100)
    print('Question: ', number)
    return number
