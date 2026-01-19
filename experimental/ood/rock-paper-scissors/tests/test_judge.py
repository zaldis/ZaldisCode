from src.core.game import judge_winner
from src.core.models import GameMove, JudgeVerdict


def test_same_game_move__draw():
    assert judge_winner(GameMove.SCISSORS, GameMove.SCISSORS) == JudgeVerdict.DRAW
    assert judge_winner(GameMove.PAPER, GameMove.PAPER) == JudgeVerdict.DRAW
    assert judge_winner(GameMove.ROCK, GameMove.ROCK) == JudgeVerdict.DRAW

def test_scissors_rock__rock_win():
    assert judge_winner(GameMove.SCISSORS, GameMove.ROCK) == JudgeVerdict.SECOND_PLAYER

def test_scissors_paper__scissors_win():
    assert judge_winner(GameMove.SCISSORS, GameMove.PAPER) == JudgeVerdict.FIRST_PLAYER

def test_rock_scissors__rock_win():
    assert judge_winner(GameMove.ROCK, GameMove.SCISSORS) == JudgeVerdict.FIRST_PLAYER

def test_rock_paper__paper_win():
    assert judge_winner(GameMove.ROCK, GameMove.PAPER) == JudgeVerdict.SECOND_PLAYER

def test_paper_scissors__scissors_win():
    assert judge_winner(GameMove.PAPER, GameMove.SCISSORS) == JudgeVerdict.SECOND_PLAYER

def test_paper_rock__paper_win():
    assert judge_winner(GameMove.PAPER, GameMove.ROCK) == JudgeVerdict.FIRST_PLAYER