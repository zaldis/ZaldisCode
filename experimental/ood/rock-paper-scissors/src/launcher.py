from enum import StrEnum
from threading import Thread
from typing import Protocol

from src.core.game import random_choice_move_strategy, Game
from src.core.protocols import GameSettings, Player, UI
from src.ui.emoji_based_console import EmojiBasedConsole
from src.ui.text_based_console import TextBasedConsoleUI
from src.ui.tkinter_based_window import TkinterBasedConsole


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
            GameTheme.CONSOLE: _DefaultGameLauncher,
            GameTheme.EMOJI: _DefaultGameLauncher,
            GameTheme.TKINTER: _TkinterGameLauncher,
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
            win_rounds=10,
            ui=self._ui_engines[theme]()
        )
        game = Game(settings)
        return self._launchers[theme](game, settings.ui)


class _DefaultGameLauncher(GameLauncher):
    def __init__(self, game: Game, ui: UI):
        self._game = game
        self._ui = ui

    def launch(self) -> None:
        self._game.start_game()

class _TkinterGameLauncher(GameLauncher):
    def __init__(self, game: Game, ui: TkinterBasedConsole):
        self._game = game
        self._ui = ui

    def launch(self) -> None:
        game_thread = Thread(target=lambda: self._game.start_game(), daemon=True)
        game_thread.start()
        self._ui.render()