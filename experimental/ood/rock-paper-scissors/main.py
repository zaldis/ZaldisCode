import argparse
from src.launcher import GameLauncherFactory, GameTheme


def launch_rock_paper_scissors():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t', "--theme",
        choices=["console", "emoji", "tkinter"], default="emoji", help="Game UI engine.")
    parser.add_argument(
        '-n1', "--name1",
        default="bot-oleg", help="The name of the first player.")
    parser.add_argument(
        '-m1', "--mode1",
        choices=["human", "bot"], default="bot", help="Who is control the first player.")
    parser.add_argument(
        '-n2', "--name2",
        default="bot-ivan", help="The name of the second player.")
    parser.add_argument(
        '-m2', "--mode2",
        choices=["human", "bot"], default="bot", help="Who is control the second player.")
    args = parser.parse_args()

    game_launcher_factory = GameLauncherFactory()
    game_launcher = game_launcher_factory.build(
        theme=GameTheme(args.theme),
        first_player_name=args.name1,
        is_first_player_bot=(args.mode1 == 'bot'),
        second_player_name=args.name2,
        is_second_player_bot=(args.mode2 == 'bot')
    )
    game_launcher.launch()


if __name__ == '__main__':
    launch_rock_paper_scissors()