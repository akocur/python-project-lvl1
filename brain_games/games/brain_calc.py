from random import randint
from random import choice


def show_game_rules():
    """Show game rules."""
    print("What is the result of the expression?")


def ask_question():
    """Ask question. First, second numbers and operation are chosen randomly.

    :returns:
        tuple number_one, operation, number_two
    :rtype
        (int, string, int)
    """
    number_one = randint(0, 100)
    number_two = randint(0, 100)
    available_operation = '+-*'
    operation = choice(available_operation)
    expression = '{0} {1} {2}'.format(number_one, operation, number_two)
    print('Question: ', expression)
    return number_one, operation, number_two
