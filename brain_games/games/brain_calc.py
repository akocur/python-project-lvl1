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
    print('Question:', expression)
    return number_one, operation, number_two


def get_correct_answer(question):
    """Get correct answer on question

    :param (int, string, int) question:
        Question in the form of tuple number_one, operation, number_two
    :returns:
        Correct answer on question
    :rtype:
        str
    """
    number_one, operation, number_two = question
    return str(evaluate_expression(number_one, operation, number_two))


def evaluate_expression(number_one, operation, number_two):
    """Evaluate expression

    :param int number_one:
        First number.
    :param str operation:
        Operation. Available + - *
    :param int number_two:
        Second number.
    :return:
        Result of the expression.
    :rtype:
        int
    """
    if operation == '+':
        return number_one + number_two
    if operation == '-':
        return number_one - number_two
    if operation == '*':
        return number_one * number_two
    raise RuntimeError('Failed to evaluate expression. Unknown operation {0}'
                       .format(operation))
