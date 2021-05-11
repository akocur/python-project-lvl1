answer_yes = 'yes'
answer_no = 'no'


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
