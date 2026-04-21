
import tkinter as tk
from tkinter import font, ttk

from logic import GameLogic

# colour constants
DEFAULT_BG = "#f0f4f8"
MAIN_TEXT = "#334155"
BORDERS = "#d1d9e6"

TEXT_FAMILY = "Helvetica"


class DartsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Darts Scorer")
        self.resizable(True, True)
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # logic.py
        self.logic = GameLogic()

        # HOME FRAME
        self.home_frame = ttk.Frame(self, style="home_frame.TFrame")
        self.home_frame.place(
            relx=0,
            relwidth=0.5,
            relheight=1
        )
        self.style.configure("home_frame.TFrame", background=DEFAULT_BG)
        home_away_headers = font.Font(
            family=TEXT_FAMILY, size=70, underline=True, weight="bold"
        )
        # HOME HEADER
        self.home_label = ttk.Label(
            self.home_frame,
            style="home_label.TLabel",
            text="HOME",
            font=home_away_headers,
            background=DEFAULT_BG,
            foreground=MAIN_TEXT,
            anchor="center"
        )
        self.home_label.place(
            relwidth=1,
            height=100,
            relx=0,
            rely=0,
            y=15,
        )

        # HOME REMAINING
        home_remaining_header_font = font.Font(
            family=TEXT_FAMILY, size=15, weight="bold"
        )
        self.home_remaining_header = ttk.Label(
            self.home_frame,
            style="home_remaining.TLabel",
            text="REMAINING",
            font=home_remaining_header_font,
            foreground=MAIN_TEXT,
            background=DEFAULT_BG,
            anchor="center"
        )
        self.home_remaining_header.place(
            relwidth=1,
            relx=0,
            y=200
        )
        home_remaining_value_font = font.Font(
            family=TEXT_FAMILY, size=120, weight="bold"
        )
        # TODO: fix the gap beneath the bottom of the number
        self.home_remaining_value = ttk.Label(
            self.home_frame,
            style="home_remaining_value.TLabel",
            text=self.logic.home.remaining,
            font=home_remaining_value_font,
            foreground=MAIN_TEXT,
            background=DEFAULT_BG if self.logic.active_player != self.logic.home else "#c3f7c8",
            anchor="center"
        )
        self.home_remaining_value.place(
            relx=0.5,
            rely=0.3,
            anchor="center"
        )

        # AWAY FRAME
        self.away_frame = ttk.Frame(self, style="away_frame.TFrame")
        self.away_frame.place(
            relx=0.5,
            relwidth=0.5,
            relheight=1
        )
        self.style.configure("away_frame.TFrame", background=DEFAULT_BG)

        # MODE & FORMAT BAR
        self.mode_format_bar = ttk.Label(
            self,
            style="mode_format_bar.TLabel",
            border=True,
            borderwidth=2,
            relief="solid"
        )
        self.style.configure(
            "mode_format_bar.TLabel",
            background=DEFAULT_BG,
            bordercolor=BORDERS,
            lightcolor=BORDERS,
            darkcolor=BORDERS
        )
        self.mode_format_bar.place(
            relwidth=1,
            height=50,
            y=115,
        )

        mode_format_headers = font.Font(
            family=TEXT_FAMILY, size=15, underline=False, weight="bold", slant="italic"
        )

        # MODE
        self.mode_header = ttk.Label(
            self.mode_format_bar,
            style="mode_header.TLabel",
            text="MODE:",
            font=mode_format_headers,
            background=DEFAULT_BG,
            foreground=MAIN_TEXT,
            anchor="center"
        )
        self.mode_header.place(
            width=100,
            relx=0.4,
            rely=0.5,
            anchor="center"
        )

        # FORMAT
        self.format_header = ttk.Label(
            self.mode_format_bar,
            style="format_header.TLabel",
            text="FORMAT:",
            font=mode_format_headers,
            background=DEFAULT_BG,
            foreground=MAIN_TEXT,
            anchor="center"
        )
        self.format_header.place(
            width=100,
            relx=0.6,
            rely=0.5,
            anchor="center"
        )

    def run(self):
        """Runs the gui"""
        self.mainloop()
