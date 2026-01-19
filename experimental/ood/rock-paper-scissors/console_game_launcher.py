from src.core.game import random_choice_move_strategy, Game
from src.core.models import GameSettings, Player
from src.ui.text_based_console import TextBasedConsoleUI


if __name__ == '__main__':
    settings = GameSettings(
        first_player=Player("Ivan", is_bot=True),
        second_player=Player("Denys", is_bot=True),
        bot_strategy=random_choice_move_strategy,
        win_rounds=3,
        ui=TextBasedConsoleUI()
    )
    game = Game(settings)
    game.start_game()