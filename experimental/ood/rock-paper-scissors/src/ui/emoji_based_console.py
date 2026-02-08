from src.core.models import GameMove, GameState, Player
from src.core.protocols import UI


class EmojiBasedConsole(UI):
    def ask_user_move(self) -> GameMove:
        input_maps = {
            1: GameMove.ROCK,
            2: GameMove.PAPER,
            3: GameMove.SCISSORS
        }
        user_input = int(input("Enter your choice 1-✊(rock); 2-✋(paper); 3-✌️(scissors): "))
        return input_maps[user_input]

    def display_game_state(self, state: GameState) -> None:
        game_move_maps = {
            GameMove.ROCK: '✊',
            GameMove.PAPER: '✋',
            GameMove.SCISSORS: '✌️'
        }
        print(f"({state.first_player.name}) {game_move_maps[state.first_player_move]} 𓊳 {game_move_maps[state.second_player_move]} ({state.second_player.name})")
        print(
            f"Played games: {state.number_of_played_games};"
            f"\t{state.first_player.name} wins: {state.first_player_score};"
            f"\t{state.second_player.name} wins: {state.second_player_score}"
        )

    def display_game_over(self, winner: Player):
        print(f"{winner.name} has won! Congrats!")
