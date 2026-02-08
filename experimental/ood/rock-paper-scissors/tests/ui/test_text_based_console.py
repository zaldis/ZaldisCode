from src.ui.text_based_console import TextBasedConsoleUI
from src.core.models import Player


def test_game_over_message__contains_winner_name(capsys) -> None:
    ui = TextBasedConsoleUI()
    player = Player(name="Champ", is_bot=False)

    ui.display_game_over(winner=player)

    assert "Champ has won! Congrats!" in capsys.readouterr().out