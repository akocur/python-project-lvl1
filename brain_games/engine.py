import prompt


def get_answer():
    """Get user answer.

    :returns:
        User answer.
    :rtype:
        str
    """
    return prompt.string('Your answer: ')
