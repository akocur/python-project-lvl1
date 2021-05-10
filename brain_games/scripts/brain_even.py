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


if __name__ == '__main__':
    main()
