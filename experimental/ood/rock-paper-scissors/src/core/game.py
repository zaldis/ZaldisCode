import random

from src.core.models import GameMove, GameSettings, Player, JudgeVerdict


class Game:
    def __init__(self, settings: GameSettings):
        self._games = 0
        self._settings = settings
        self._score_table = {
            self.first_player: 0,
            self.second_player: 0
        }

    @property
    def first_player(self) -> Player:
        return self._settings.first_player

    @property
    def second_player(self) -> Player:
        return self._settings.second_player

    @property
    def bot_strategy(self):
        return self._settings.bot_strategy

    @property
    def ask_user_move(self):
        return self._settings.ui.ask_user_move

    def start_game(self) -> None:
        while not self._is_game_over():
            first_player_move = self.bot_strategy() if self.first_player.is_bot else self.ask_user_move()
            second_player_move = self.bot_strategy() if self.second_player.is_bot else self.ask_user_move()
            verdict = judge_winner(first_player_move, second_player_move)
            if verdict == JudgeVerdict.FIRST_PLAYER:
                self._score_table[self.first_player] += 1
            if verdict == JudgeVerdict.SECOND_PLAYER:
                self._score_table[self.second_player] += 1
            self._games += 1
            self._settings.ui.display_game_state(self._score_table, self._games, first_player_move, second_player_move)
        self._settings.ui.display_game_over(self._find_winner())

    def _find_winner(self) -> Player:
        if not self._is_game_over():
            raise ValueError("No winner!")
        if self._score_table[self.first_player] >= self._settings.win_rounds:
            return self.first_player
        return self.second_player

    def _is_game_over(self) -> bool:
        return (
            self._score_table[self.first_player] >= self._settings.win_rounds
            or self._score_table[self.second_player] >= self._settings.win_rounds
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
