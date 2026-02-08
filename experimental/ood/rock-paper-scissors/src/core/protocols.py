from dataclasses import dataclass
from typing import Protocol, Callable

from .models import GameMove, GameState


@dataclass
class Player:
    name: str
    is_bot: bool


class UI(Protocol):
    def ask_user_move(self) -> GameMove: ...
    def display_game_state(self, state: GameState) -> None: ...
    def display_game_over(self, winner: Player): ...


@dataclass
class GameSettings:
    BotMoveStrategy = Callable[[], GameMove]

    first_player: Player
    second_player: Player
    bot_strategy: BotMoveStrategy
    win_rounds: int
    ui: UI
