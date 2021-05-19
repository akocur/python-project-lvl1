from random import randint


def show_game_rules():
    """Show game rules."""
    print("Find the greatest common divisor of given numbers.")


def ask_question():
    """Ask question. First, second numbers are chosen randomly.

    :returns:
        tuple number_one, number_two
    :rtype
        (int, int)
    """
    number_one = randint(0, 100)
    number_two = randint(0, 100)
    expression = '{0} {1}'.format(number_one, number_two)
    print('Question: ', expression)
    return number_one, number_two
