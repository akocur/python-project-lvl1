#!/usr/env python3
"""Brain game progression."""

import brain_games.games.brain_progression as brain_progression
import brain_games.engine as engine


def main():
    """Entry point."""
    engine.run(brain_progression)


if __name__ == '__main__':
    main()
