import prompt
from random import randint

answer_yes = 'yes'
answer_no = 'no'


def welcome_user():
    """Asks for a name and greets.

        Returns:
            string: user name
        """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421
    print('Answer "{0}" if the number is even, otherwise answer "{1}".'
          .format(answer_yes, answer_no))
    return name


def ask_question():
    """Ask a question to the user.

    :returns:
        Number to determine whether it is even or not.
    :rtype:
        int
    """
    number = randint(0, 100)  # noqa: S311
    print('Question:', number)
    return number


def get_correct_answer(question):
    """Get correct answer.

    :returns:
        "yes" if question is even number else "no"
    :rtype:
        str
    """
    global answer_yes, answer_no
    return answer_yes if is_even_number(question) else answer_no


def is_even_number(number):
    """Check if number is even.

    :param int number:
        Any number.
    :returns:
        True if number is even else False.
    :rtype:
        bool
    """
    return number % 2 == 0
