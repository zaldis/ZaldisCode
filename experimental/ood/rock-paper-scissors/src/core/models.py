from enum import StrEnum
from dataclasses import dataclass


class GameMove(StrEnum):
    ROCK = 'Rock'
    SCISSORS = 'Scissors'
    PAPER = 'Paper'


class JudgeVerdict(StrEnum):
    FIRST_PLAYER = 'FirstPlayer'
    SECOND_PLAYER = 'SecondPlayer'
    DRAW = 'Draw'


@dataclass
class Player:
    name: str
    is_bot: bool

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name


@dataclass
class GameState:
    number_of_played_games: int

    first_player: Player
    first_player_move: GameMove
    first_player_score: int

    second_player: Player
    second_player_move: GameMove
    second_player_score: int
