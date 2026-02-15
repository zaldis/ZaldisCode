import tkinter as tk
from pathlib import Path
from tkinter import ttk, PhotoImage, scrolledtext
from queue import Queue
from enum import StrEnum

from src.core.models import GameMove, GameState, Player
from src.core.protocols import UI

current_dir = Path(__file__).resolve().parent

class _ButtonState(StrEnum):
    NORMAL = 'normal'
    DISABLED = 'disabled'

class _GameMove(StrEnum):
    ROCK = 'Rock'
    PAPER = 'Paper'
    SCISSORS = 'Scissors'

class TkinterBasedConsole(UI):
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.mainframe = ttk.Frame(self.root,  padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=tk.NSEW)
        self.mainframe.columnconfigure((0, 1, 2), weight=1)
        self.label = ttk.Label(self.mainframe, text="> Choose your move", font=("Arial", 12))
        self.label.grid(column=0, row=0, columnspan=3)
        style = ttk.Style()
        bg_color = style.lookup("TFrame", "background")
        self.game_log_widget = scrolledtext.ScrolledText(self.mainframe, width=70, height=15, background=bg_color)
        self.game_log_widget.grid(row=2, column=0, columnspan=3)

        self.rock_image = PhotoImage(file=str(current_dir / 'assets' / 'rock.png'))
        self.selected_rock_image = PhotoImage(file=str(current_dir / 'assets' / 'rock-selected.png'))
        self.scissors_image = PhotoImage(file=str(current_dir / 'assets' / 'scissors.png'))
        self.selected_scissors_image = PhotoImage(file=str(current_dir / 'assets' / 'scissors-selected.png'))
        self.paper_image = PhotoImage(file=str(current_dir / 'assets' / 'paper.png'))
        self.selected_paper_image = PhotoImage(file=str(current_dir / 'assets' / 'paper-selected.png'))

        self.inputs = Queue()
        self.events = Queue()

        self.moves = {}
        for col, choice in enumerate(
                [_GameMove.ROCK, _GameMove.PAPER, _GameMove.SCISSORS],
                start=0
        ):
            move_label = ttk.Label(
                self.mainframe,
                image=self._get_game_move_image(choice),
                text=choice.value.capitalize(),
                cursor="hand2",
                state=_ButtonState.DISABLED.value
            )
            if choice == _GameMove.ROCK:
                move_label.bind("<Enter>", self.on_rock_enter)
                move_label.bind("<Leave>", self.on_rock_leave)
            if choice == _GameMove.PAPER:
                move_label.bind("<Enter>", self.on_paper_enter)
                move_label.bind("<Leave>", self.on_paper_leave)
            if choice == _GameMove.SCISSORS:
                move_label.bind("<Enter>", self.on_scissors_enter)
                move_label.bind("<Leave>", self.on_scissors_leave)
            move_label.bind("<Button-1>", lambda event, c=choice: self._on_button_click(c))
            move_label.grid(column=col, row=1, padx=10)
            self.moves[choice] = move_label
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
        player1_move = _get_game_move_emoji(_GameMove(state.first_player_move))
        player2_move = _get_game_move_emoji(_GameMove(state.second_player_move))
        self.events.put(
            f"#{state.number_of_played_games}: ({state.first_player.name} - {state.first_player_score}) {player1_move} "
            f"- {player2_move} ({state.second_player.name} - {state.second_player_score})"
        )

    def display_game_over(self, winner: Player):
        self.events.put(f"{winner.name} has won! Congrats!")

    def _on_button_click(self, choice):
        self.inputs.put(choice)

    def _process_events(self):
        while not self.events.empty():
            event_name = self.events.get()
            if event_name == "enable_buttons":
                self._set_buttons_state(_ButtonState.NORMAL)
            elif event_name == "disable_buttons":
                self._set_buttons_state(_ButtonState.DISABLED)
            else:
                self._update_game_log(event_name)
        self.root.after(100, self._process_events)

    def _set_buttons_state(self, state: _ButtonState):
        for btn in self.moves.values():
            btn.config(state=state.value)

    def _update_game_log(self, message: str):
        self.game_log_widget.config(state="normal")
        self.game_log_widget.insert("1.0", message + '\n')
        self.game_log_widget.see("1.0")
        self.game_log_widget.config(state="disabled")

    def _get_game_move_image(self, move: _GameMove) -> PhotoImage:
        move_image = {
            _GameMove.PAPER: self.paper_image,
            _GameMove.SCISSORS: self.scissors_image,
            _GameMove.ROCK: self.rock_image,
        }
        return move_image[move]

    def on_rock_enter(self, event):
        event.widget.config(image=self.selected_rock_image)

    def on_rock_leave(self, event):
        event.widget.config(image=self.rock_image)

    def on_paper_enter(self, event):
        event.widget.config(image=self.selected_paper_image)

    def on_paper_leave(self, event):
        event.widget.config(image=self.paper_image)

    def on_scissors_enter(self, event):
        event.widget.config(image=self.selected_scissors_image)

    def on_scissors_leave(self, event):
        event.widget.config(image=self.scissors_image)

def _get_game_move_emoji(move: _GameMove) -> str:
    move_emoji = {
        _GameMove.PAPER: "✋",
        _GameMove.SCISSORS: "✌️",
        _GameMove.ROCK: "✊",
    }
    return move_emoji[move]

