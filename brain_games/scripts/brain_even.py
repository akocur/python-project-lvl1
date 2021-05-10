"""Brain even."""

from random import randint

import prompt
from brain_games.cli import welcome_user

answer_yes = 'yes'
answer_no = 'no'


def main():
    """Entry point."""
    user_name = welcome_user()
    global answer_yes, answer_no
    print('Answer "{0}" if the number is even, otherwise answer "{1}".'
          .format(answer_yes, answer_no))
    question_count = 3
    for _ in range(question_count):
        question = ask_question()
        answer = get_answer()
        if not is_correct_answer(question, answer):
            game_over(user_name, answer, get_correct_answer(question))
            break
        print('Correct!')
    else:
        congratulations(user_name)


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


def get_answer():
    """Get user answer.

    :returns:
        User answer.
    :rtype:
        str
    """
    return prompt.string('Your answer: ')


def game_over(user_name, answer, correct_answer):
    """Print messages when user lose.

    :param str user_name:
        User name.
    :param str answer:
        User answer.
    :param str correct_answer:
        Correct answer.
    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'."
          .format(answer, correct_answer))
    print("Let's try again, {0}!".format(user_name))


def is_correct_answer(question, answer):
    """Check if the answer is correct.

    :param int question:
        Any integer number. See ask_question() function.
    :param str answer:
        User answer. See get_answer() function.
    :returns:
        True if answer is correct else False
    :rtype:
        bool
    """
    correct_answer = get_correct_answer(question)
    return correct_answer == answer


def congratulations(user_name):
    """Print message when user is win."""
    print('Congratulations, {0}!'.format(user_name))


if __name__ == '__main__':
    main()
