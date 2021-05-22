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


def get_correct_answer(question):
    """Get correct answer on question

    :param int question:
        Question. see ask_question() function
    :returns:
        Correct answer on question
    :rtype:
        str
    """
    correct_question = 'yes' if is_prime(question) else 'no'
    return correct_question


def is_prime(number):
    """Check whether the number is prime.

    :param int number:
    :returns:
        True if the number is prime else False
    :rtype:
        bool
    """
    if number <= 1:
        return False
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            return False
    return True
