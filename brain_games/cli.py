"""Command Line Interface."""
import prompt


def welcome_user():
    """Asks for a name and greets.

    Returns:
        string: user name
    """
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421
    return name
