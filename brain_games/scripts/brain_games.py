#!/usr/bin/env python3
"""Brain games."""
from brain_games.cli import welcome_user

user_name = None


def main():
    """Entry point."""
    print('Welcome to the Brain Games!')
    global user_name
    user_name = welcome_user()


if __name__ == '__main__':
    main()
