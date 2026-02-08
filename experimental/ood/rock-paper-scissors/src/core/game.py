import random

from .models import GameMove, Player, JudgeVerdict, GameState
from .protocols import GameSettings


class Game:
    def __init__(self, settings: GameSettings):
        self._games = 0
        self._settings = settings
        self._first_player = Player(name=settings.first_player.name, is_bot=settings.first_player.is_bot)
        self._second_player = Player(name=settings.second_player.name, is_bot=settings.second_player.is_bot)
        self._score_table = {
            self._first_player: 0,
            self._second_player: 0
        }

    @property
    def bot_strategy(self):
        return self._settings.bot_strategy

    def start_game(self) -> None:
        while not self._is_game_over():
            self._play_game_round()
        self._display_game_over(self._find_winner())

    def _play_game_round(self) -> None:
        first_player_move = self.bot_strategy() if self._first_player.is_bot else self._ask_user_move()
        second_player_move = self.bot_strategy() if self._second_player.is_bot else self._ask_user_move()
        verdict = judge_winner(first_player_move, second_player_move)
        if verdict == JudgeVerdict.FIRST_PLAYER:
            self._score_table[self._first_player] += 1
        if verdict == JudgeVerdict.SECOND_PLAYER:
            self._score_table[self._second_player] += 1
        self._games += 1
        game_state = self._build_game_state(first_player_move, second_player_move)
        self._display_game_state(game_state)

    def _find_winner(self) -> Player:
        if not self._is_game_over():
            raise ValueError("No winner!")
        if self._score_table[self._first_player] >= self._settings.win_rounds:
            return self._first_player
        return self._second_player

    def _is_game_over(self) -> bool:
        return (
            self._score_table[self._first_player] >= self._settings.win_rounds
            or self._score_table[self._second_player] >= self._settings.win_rounds
        )

    def _ask_user_move(self):
        return self._settings.ui.ask_user_move()

    def _display_game_state(self, state: GameState) -> None:
        return self._settings.ui.display_game_state(state)

    def _display_game_over(self, winner: Player) -> None:
        return self._settings.ui.display_game_over(winner)

    def _build_game_state(self, first_player_move: GameMove, second_player_move: GameMove) -> GameState:
       return GameState(
           number_of_played_games=self._games,
           first_player=self._first_player,
           first_player_move=first_player_move,
           first_player_score=self._score_table[self._first_player],

           second_player=self._second_player,
           second_player_move=second_player_move,
           second_player_score=self._score_table[self._second_player]
       )

def random_choice_move_strategy() -> GameMove:
    return random.choice(list(GameMove))

def judge_winner(first_player_move: GameMove, second_player_move: GameMove) -> JudgeVerdict:
    if first_player_move == second_player_move:
        return JudgeVerdict.DRAW
    if first_player_move == GameMove.ROCK:
        return JudgeVerdict.FIRST_PLAYER if second_player_move == GameMove.SCISSORS else JudgeVerdict.SECOND_PLAYER
    if first_player_move == GameMove.PAPER:
        return JudgeVerdict.FIRST_PLAYER if second_player_move == GameMove.ROCK else JudgeVerdict.SECOND_PLAYER
    if first_player_move == GameMove.SCISSORS:
        return JudgeVerdict.FIRST_PLAYER if second_player_move == GameMove.PAPER else JudgeVerdict.SECOND_PLAYER
    raise ValueError(
        f"Unexpected game state. First player move {first_player_move}; "
        f"Second player move {second_player_move}"
    )
