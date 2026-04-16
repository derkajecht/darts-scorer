
import tkinter as tk
from tkinter import ttk

from logic import GameLogic


class DartsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Darts Scorer")
        self.logic = GameLogic()

        # Add widgets

    def run(self):
        """Runs the gui and allows it to be called from main.py"""
        self.root.mainloop()
