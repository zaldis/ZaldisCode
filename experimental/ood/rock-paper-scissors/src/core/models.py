from enum import StrEnum
from dataclasses import dataclass
from typing import Callable


class GameMove(StrEnum):
    ROCK = 'Rock'
    SCISSORS = 'Scissors'
    PAPER = 'Paper'


@dataclass
class Player:
    name: str
    is_bot: bool

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


class JudgeVerdict(StrEnum):
    FIRST_PLAYER = 'FirstPlayer'
    SECOND_PLAYER = 'SecondPlayer'
    DRAW = 'Draw'

@dataclass
class GameSettings:
    from .protocols import UI
    BotMoveStrategy = Callable[[], GameMove]

    first_player: Player
    second_player: Player
    bot_strategy: BotMoveStrategy
    win_rounds: int
    ui: UI
