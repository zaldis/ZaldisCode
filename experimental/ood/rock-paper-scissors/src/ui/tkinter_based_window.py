import tkinter as tk
from queue import Queue

from src.core.models import GameMove, GameState, Player
from src.core.protocols import UI


class TkinterBasedConsole(UI):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")

        self.label = tk.Label(self.root, text="> Choose your move", font=("Arial", 12))
        self.label.pack(pady=10)

        self.inputs = Queue()
        self.events = Queue()

        self.buttons = {}
        for choice in ["Rock", "Paper", "Scissors"]:
            btn = tk.Button(
                self.root,
                text=choice.capitalize(),
                command=lambda c=choice: self._on_button_click(c),
                state="disabled"
            )
            btn.pack(side="left", padx=10, pady=20)
            self.buttons[choice] = btn
        self.root.after(100, self._process_events)

    def render(self):
        self.root.mainloop()

    def ask_user_move(self) -> GameMove:
        self.events.put("enable_buttons")

        # Block and execution thread until something appears in input_queue
        user_choice = self.inputs.get()

        self.events.put("disable_buttons")
        return GameMove(user_choice)

    def display_game_state(self, state: GameState) -> None:
        self.events.put(
            f"#{state.number_of_played_games}: ({state.first_player.name} - {state.first_player_score}) {state.first_player_move} - {state.second_player_move} ({state.second_player.name} - {state.second_player_score})"
        )

    def display_game_over(self, winner: Player):
        self.events.put(f"{winner.name} has won! Congrats!")

    def _on_button_click(self, choice):
        """Callback for the buttons."""
        self.inputs.put(choice)

    def _process_events(self):
        while not self.events.empty():
            msg = self.events.get()
            if msg == "enable_buttons":
                self._set_buttons_state("normal")
            elif msg == "disable_buttons":
                self._set_buttons_state("disabled")
            else:
                self.label.config(text=msg)
        self.root.after(100, self._process_events)

    def _set_buttons_state(self, state):
        """Utility to enable/disable all buttons."""
        for btn in self.buttons.values():
            btn.config(state=state)
