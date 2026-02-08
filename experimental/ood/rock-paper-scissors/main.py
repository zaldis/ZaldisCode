import argparse
from threading import Thread
from enum import StrEnum
from typing import Protocol

from src.core.game import random_choice_move_strategy, Game
from src.core.protocols import GameSettings, Player, UI
from src.ui.tkinter_based_window import TkinterBasedConsole
from src.ui.emoji_based_console import EmojiBasedConsole
from src.ui.text_based_console import TextBasedConsoleUI


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


class GameTheme(StrEnum):
    CONSOLE = 'console'
    EMOJI = 'emoji'
    TKINTER = 'tkinter'


class GameLauncher(Protocol):
    def launch(self) -> None:
        pass


class GameLauncherFactory:
    def __init__(self) -> None:
        self._ui_engines = {
            GameTheme.CONSOLE: TextBasedConsoleUI,
            GameTheme.EMOJI: EmojiBasedConsole,
            GameTheme.TKINTER: TkinterBasedConsole
        }
        self._launchers = {
            GameTheme.CONSOLE: DefaultGameLauncher,
            GameTheme.EMOJI: DefaultGameLauncher,
            GameTheme.TKINTER: TkinterGameLauncher,
        }

    def build(
        self,
        theme: GameTheme,
        first_player_name: str, is_first_player_bot: bool, second_player_name: str, is_second_player_bot: bool
    ) -> GameLauncher:
        settings = GameSettings(
            first_player=Player(first_player_name, is_bot=is_first_player_bot),
            second_player=Player(second_player_name, is_bot=is_second_player_bot),
            bot_strategy=random_choice_move_strategy,
            win_rounds=3,
            ui=self._ui_engines[theme]()
        )
        game = Game(settings)
        return self._launchers[theme](game, settings.ui)


class DefaultGameLauncher(GameLauncher):
    def __init__(self, game: Game, ui: UI):
        self._game = game
        self._ui = ui

    def launch(self) -> None:
        self._game.start_game()

class TkinterGameLauncher(GameLauncher):
    def __init__(self, game: Game, ui: TkinterBasedConsole):
        self._game = game
        self._ui = ui

    def launch(self) -> None:
        game_thread = Thread(target=lambda: self._game.start_game(), daemon=True)
        game_thread.start()
        self._ui.render()


if __name__ == '__main__':
    launch_rock_paper_scissors()