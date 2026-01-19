from src.core.models import GameMove, Player
from src.core.protocols import UI


class TextBasedConsoleUI(UI):
    def ask_user_move(self) -> GameMove:
        input_maps = {
            1: GameMove.ROCK,
            2: GameMove.PAPER,
            3: GameMove.SCISSORS
        }
        user_input = int(input("Enter your choice (1-rock; 2-paper; 3-scissors): "))
        return input_maps[user_input]

    def display_game_state(self, score_table: dict[Player, int], games: int, first_player_move: GameMove, second_player_move: GameMove) -> None:
        print(f"{first_player_move} - {second_player_move}")
        first_player, second_player = score_table.keys()
        print(f"Played games: {games};\t{first_player.name} wins: {score_table[first_player]};\t{second_player.name} wins: {score_table[second_player]}")

    def display_game_over(self, winner: Player):
        print(f"{winner.name} has won! Congrats!")
