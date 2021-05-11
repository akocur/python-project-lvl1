import prompt


def run(game_module):
    """
    Run game
    :param game_module:
        Game module.
    :return:
    """
    user_name = game_module.welcome_user()
    question_count = 3
    for _ in range(question_count):
        question = game_module.ask_question()
        answer = get_answer()
        if not is_correct_answer(game_module, question, answer):
            game_over(user_name, answer, game_module.get_correct_answer(question))
            break
        print('Correct!')
    else:
        congratulations(user_name)


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


def is_correct_answer(game_module, question, answer):
    """Check if the answer is correct.

    :param game_module:
        Game module.
    :param int question:
        Any integer number. See ask_question() function.
    :param str answer:
        User answer. See get_answer() function.
    :returns:
        True if answer is correct else False
    :rtype:
        bool
    """
    correct_answer = game_module.get_correct_answer(question)
    return correct_answer == answer


def congratulations(user_name):
    """Print message when user is win."""
    print('Congratulations, {0}!'.format(user_name))
