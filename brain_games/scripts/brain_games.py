#!/usr/bin/env python3


from brain_games.cli import welcome_user

player_name = None


def main():
    global player_name
    player_name = welcome_user()


if __name__ == '__main__':
    main()
