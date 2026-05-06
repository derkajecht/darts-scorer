
import tkinter as tk
from tkinter import ttk

import customtkinter as ctk

from logic import GameLogic

# colour constants
DEFAULT_BG = "#f0f4f8"
DATA_TEXT = "#1e1e1e"
MAIN_TEXT = "#334155"
BORDERS = "#d1d9e6"
DATA_BG = "#ffffff"

TEXT_FAMILY = "Helvetica"

# font styling
home_header = (TEXT_FAMILY, 80, "bold")
home_remaining_header_font = (TEXT_FAMILY, 25, "bold")
home_remaining_value_font = (TEXT_FAMILY, 150, "bold")
mode_format_headers = (TEXT_FAMILY, 15, "bold italic")
mode_format_value = (TEXT_FAMILY, 35, "bold")
leg_avg_throw_font = (TEXT_FAMILY, 45, "bold")
leg_avg_value_font = (TEXT_FAMILY, 50, "bold")
checkout_header_font = (TEXT_FAMILY, 45, "bold")
checkout_value_font = (TEXT_FAMILY, 50, "bold")
sets_legs_header_font = (TEXT_FAMILY, 25, "bold")
sets_legs_value_font = (TEXT_FAMILY, 55, "bold")


class DartsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # logic.py
        self.logic = GameLogic()

        self.title("Darts Scorer")
        self.resizable(True, True)
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # HOME FRAME
        self.home_frame = ttk.Frame(
            self,
            style="home_frame.TFrame",
            border=True,
            borderwidth=2
        )
        self.home_frame.place(
            relx=0,
            relwidth=0.5,
            relheight=1
        )
        self.style.configure("home_frame.TFrame", background=DEFAULT_BG)

        # HOME HEADER
        self.home_label = ctk.CTkLabel(
            self.home_frame,
            text="HOME",
            font=home_header,
            fg_color=DEFAULT_BG,
            text_color=MAIN_TEXT,
            anchor="center",
            width=100,
            height=100
        )
        self.home_label.place(
            relwidth=1,
            relx=0.5,
            rely=0.04,
            y=25,
            anchor="center",
        )

        # HOME REMAINING
        self.home_remaining_header = ctk.CTkLabel(
            self.home_frame,
            text="REMAINING",
            font=home_remaining_header_font,
            text_color=MAIN_TEXT,
            fg_color=DEFAULT_BG,
            anchor="center"
        )
        self.home_remaining_header.place(
            relwidth=1,
            rely=0.2,
            relx=0.5,
            anchor="center"
        )

        # TODO: fix the gap beneath the bottom of the number
        self.home_remaining_value = ctk.CTkLabel(
            self.home_frame,
            text=str(self.logic.home.remaining),
            font=home_remaining_value_font,
            text_color=DATA_TEXT,
            fg_color=DEFAULT_BG if self.logic.active_player != self.logic.home else "#c3f7c8",
            bg_color=DEFAULT_BG,
            anchor="center",
            width=200,
            height=50,
            padx=20,
            pady=35,
            justify="center",
            corner_radius=25,
        )
        self.home_remaining_value.place(
            relx=0.5,
            rely=0.33,
            anchor="center",
        )

        # LEG AVG
        self.home_leg_avg_header = ctk.CTkLabel(
            self.home_frame,
            text="Leg Avg.",
            font=leg_avg_throw_font,
            text_color=MAIN_TEXT,
            fg_color=DEFAULT_BG,
            height=50
        )

        self.home_leg_avg_header.place(
            relx=0.5,
            rely=0.49,
            anchor="center"
        )

        self.home_leg_avg_container = ctk.CTkFrame(
            self.home_frame,
            width=250,
            height=65,
            fg_color=DATA_BG,
            border_width=4,
            border_color=BORDERS,
        )
        self.home_leg_avg_container.place(
            relx=0.5,
            rely=0.55,
            anchor="center"
        )

        self.home_leg_avg_value = ctk.CTkLabel(
            self.home_leg_avg_container,
            text=str(self.logic.home.get_average()),
            font=leg_avg_value_font,
            text_color=DATA_TEXT,
            fg_color="transparent"
        )

        self.home_leg_avg_value.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # THROW COUNT
        self.home_throw_count_header = ctk.CTkLabel(
            self.home_frame,
            text="Throw",
            font=leg_avg_throw_font,
            text_color=MAIN_TEXT,
            fg_color=DEFAULT_BG
        )
        self.home_throw_count_header.place(
            relx=0.5,
            rely=0.68,
            anchor="center"
        )
        self.home_throw_count_container = ctk.CTkFrame(
            self.home_frame,
            width=250,
            height=65,
            fg_color=DATA_BG,
            border_width=4,
            border_color=BORDERS,
        )
        self.home_throw_count_container.place(
            relx=0.5,
            rely=0.73,
            anchor="center"
        )

        self.home_throw_count_value = ctk.CTkLabel(
            self.home_throw_count_container,
            text=str(self.logic.home.throws),
            font=leg_avg_value_font,
            text_color=DATA_TEXT,
            fg_color="transparent"
        )
        self.home_throw_count_value.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # CHECKOUT
        self.home_checkout_header = ctk.CTkLabel(
            self.home_frame,
            text="Checkout",
            font=checkout_header_font,
            text_color=MAIN_TEXT,
            fg_color=DEFAULT_BG,
        )
        self.home_checkout_header.place(
            relx=0.5,
            rely=0.87,
            anchor="center"
        )

        self.home_checkout_value_container = ctk.CTkFrame(
            self.home_frame,
            width=385,
            height=65,
            fg_color=DATA_BG,
            border_width=4,
            border_color=BORDERS
        )

        self.home_checkout_value_container.place(
            relx=0.5,
            rely=0.92,
            anchor="center"
        )

        self.home_checkout_value = ctk.CTkLabel(
            self.home_checkout_value_container,
            text=str(self.logic.checkout_recs(170)),
            font=checkout_value_font,
            text_color=DATA_TEXT,
            fg_color="transparent"
        )

        self.home_checkout_value.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # SETS

        self.home_sets_header = ctk.CTkLabel(
            self.home_frame,
            text="SETS",
            font=sets_legs_header_font,
            text_color=MAIN_TEXT,
            bg_color=DEFAULT_BG,
            anchor="center",
            width=50,
            padx=3
        )

        self.home_sets_header.place(
            relx=0.12,
            rely=0.3
        )

        self.home_sets_header_container = ctk.CTkFrame(
            self.home_frame,
            width=70,
            height=75,
            fg_color=DATA_BG,
            border_width=4,
            border_color=BORDERS,
        )

        self.home_sets_header_container.place(
            relx=0.12,
            rely=0.35
        )
        self.home_sets_value = ctk.CTkLabel(
            self.home_sets_header_container,
            text=str(self.logic.home.sets),
            font=sets_legs_value_font,
            text_color=DATA_TEXT,
            fg_color=DATA_BG,
            anchor="center",
        )
        self.home_sets_value.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # LEGS
        self.home_legs_header = ttk.Label(
            self.home_frame,
            style="home_legs.TLabel",
            text="LEGS",
            font=sets_legs_header_font,
            foreground=MAIN_TEXT,
            background=DEFAULT_BG,
            anchor="center"
        )
        self.home_legs_header.place(
            width=100,
            relx=0.1,
            rely=0.6
        )
        self.home_legs_value = ttk.Label(
            self.home_frame,
            style="home_legs_value.TLabel",
            text=str(self.logic.home.legs),
            font=sets_legs_value_font,
            foreground=DATA_TEXT,
            background=DATA_BG,
            anchor="center",
            border=True,
            borderwidth=2,
            relief="solid"
        )
        self.home_legs_value.place(
            width=50,
            relx=0.13,
            rely=0.65
        )
        self.style.configure(
            "home_legs_value.TLabel",
            bordercolor=BORDERS,
            lightcolor=BORDERS,
            darkcolor=BORDERS,
            padding=(1, 15, 0, 0)
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

        self.mode_value = ttk.Label(
            self.mode_format_bar,
            style="mode_value.TLabel",
            text=self.logic.mode,
            font=mode_format_value,
            background="#fcfcca",
            foreground=MAIN_TEXT,
            anchor="center"
        )
        self.mode_value.place(
            width=100,
            x=870,
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

        self.format_value = ttk.Label(
            self.mode_format_bar,
            style="format_value.TLabel",
            text=self.logic.format,
            font=mode_format_value,
            background="#cfe4ff",
            foreground=MAIN_TEXT,
            anchor="center"
        )
        self.format_value.place(
            width=100,
            x=1270,
            rely=0.5,
            anchor="center"
        )

    def run(self):
        """Runs the gui"""
        self.mainloop()
