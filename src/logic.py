import pandas as pd

CHECKOUTS: dict[int, str] = {
    170: "T20 T20 Bull", 167: "T20 T19 Bull", 164: "T20 T18 Bull", 161: "T20 T17 Bull",
    160: "T20 T20 D20", 158: "T20 T20 D19", 157: "T20 T19 D20", 156: "T20 T20 D18",
    155: "T20 T15 Bull", 154: "T20 T18 D20", 153: "T20 T19 D18", 152: "T20 T20 D16",
    151: "T20 T17 D20", 150: "T20 T18 D18", 149: "T20 T19 D16", 148: "T20 T16 D20",
    147: "T20 T17 D18", 146: "T20 T18 D16", 145: "T20 T15 D20", 144: "T20 T20 D12",
    143: "T20 T17 D16", 142: "T20 T14 D20", 141: "T20 T15 D18", 140: "T20 T16 D16",
    139: "T20 T13 D20", 138: "T20 T14 D18", 137: "T17 T18 D16", 136: "T20 T20 D8",
    135: "T20 T15 D15", 134: "T20 T14 D16", 133: "T20 T19 D8", 132: "T20 T20 D6",
    131: "T20 T13 D16", 130: "T20 T18 D8", 129: "T20 T19 D6", 128: "T18 T14 D16",
    127: "T19 T18 D8", 126: "T19 T19 D6", 125: "B T20 D20", 124: "T20 D16 D16", 123: "T19 T16 D9",
    122: "T18 T20 D4", 121: "T20 T15 D8", 120: "T20 20 D20", 119: "T19 T10 D16", 118: "T20 18 D20",
    117: "T20 17 D20", 116: "T20 16 D20", 115: "T20 15 D20", 114: "T20 14 D20", 113: "T20 13 D20",
    112: "T20 20 D16", 111: "T20 19 D16", 110: "T20 18 D16", 109: "T20 17 D16", 108: "T20 16 D16",
    107: "T19 18 D16", 106: "T20 14 D16", 105: "T20 13 D16", 104: "T18 18 D16", 103: "T20 11 D16",
    102: "T20 10 D16", 101: "T17 18 D16", 100: "T20 D20 -", 99: "T19 10 D16", 98: "T20 D19 -",
    97: "T19 D20 -", 96: "T20 D18 -", 95: "T15 18 D16", 94: "T18 D20 -", 93: "T19 D18 -",
    92: "T20 D16 -", 91: "T17 D20 -", 90: "T18 D18 -", 89: "T19 D16 -", 88: "T16 D20 -",
    87: "T17 D18 -", 86: "T18 D16 -", 85: "T15 D20 -", 84: "T20 D12 -", 83: "T17 D16 -",
    82: "T14 D20 -", 81: "T15 D18 -", 80: "T16 D16 -", 79: "T13 D20 -", 78: "T14 D18 -",
    77: "T15 D16 -", 76: "T20 D8 -", 75: "T15 D15 -", 74: "T14 D16 -", 73: "T19 D8 -",
    72: "T20 D6 -", 71: "T13 D16 -", 70: "T18 D8 -", 69: "T19 D6 -", 68: "T16 D10 -",
    67: "T17 D8 -", 66: "T10 D18 -", 65: "T15 D10 -", 64: "D16 D16 -", 63: "T13 D12 -",
    62: "T10 D16 -", 61: "T15 D8 -", 60: "20 D20 -", 59: "19 D20 -", 58: "18 D20 -",
    57: "17 D20 -", 56: "16 D20 -", 55: "15 D20 -", 54: "14 D20 -", 53: "13 D20 -",
    52: "20 D16 -", 51: "19 D16 -", 50: "18 D16 -", 50: "Bull -", 49: "17 D16 -", 48: "16 D16 -",
    47: "15 D16 -", 46: "14 D16 -", 45: "13 D16 -", 44: "12 D16 -", 43: "11 D16 -", 42: "10 D16 -",
    41: "9 D16 -", 40: "D20 -", 39: "19 D10 -", 38: "D19 - -", 37: "5 D16 -", 36: "D18 - -",
    35: "3 D16 -", 34: "D17 - -", 33: "1 D16 -", 32: "D16 - -", 31: "15 D8 -", 30: "D15 - -",
    29: "13 D8 -", 28: "D14 - -", 27: "19 D4 -", 26: "D13 - -", 25: "17 D4 -", 24: "D12 - -",
    23: "7 D8 -", 22: "D11 - -", 21: "5 D8 -", 20: "D10 - -", 19: "11 D4 -", 18: "D9 - -",
    17: "9, D4 -", 16: "D8 - -", 15: "7 D4 -", 14: "D7 - -", 13: "5 D8 -", 12: "D6 - -",
    11: "5 D3 -", 10: "D5 - -", 9: "5 D2 -", 8: "D4 - -", 7: "3 D2 -", 6: "D3 - -", 5: "3 D1 -",
    4: "D2 - -", 3: "1 D1 -", 2: "D1 - -",
}


class Player:
    """All stats and logic for a single player"""

    def __init__(self, name: str, starting_score: int):
        self.name = name
        self.remaining = starting_score
        self.sets = 0
        self.legs = 0
        self.throws = 0
        self.scores_this_leg: list[int] = []

    def get_average(self) -> float:
        """Calculate the average score per turn for the current leg"""
        if not self.scores_this_leg:
            return 0.0
        return round(sum(self.scores_this_leg) / len(self.scores_this_leg), 2)

    def add_score(self, score: int):
        """Add a score, update remaining, increment throws, and save for average."""
        # Basic bust check
        self.remaining -= score
        self.scores_this_leg.append(score)
        self.throws += 1

    def reset_for_new_leg(self, mode: int):
        """Reset temporary stats for a new leg."""
        self.remaining = mode
        self.throws = 0
        self.scores_this_leg.clear()


class GameLogic:
    def __init__(self, mode: int = 501, format_bo: int = 3):
        self.mode = mode
        self.format = format_bo

        # Instantiate two Player objects
        self.home = Player("Home", self.mode)
        self.away = Player("Away", self.mode)
        self.leg_starter = self.home

        # Track whose turn it is
        self.active_player = self.home  # defaults to Home player
        self.non_active_player = self.away  # defaults to away player

    def set_mode(self, new_mode: int) -> str:
        """Change mode (301 or 501) and reset the game"""
        self.mode = new_mode
        self.reset_match()
        return "MODE_CHANGED"

    def switch_turn(self) -> None:
        """Swap the active player"""
        if self.active_player == self.home:
            self.active_player = self.away
            self.non_active_player = self.home
        else:
            self.active_player = self.home
            self.non_active_player = self.away

    def reset_match(self) -> str:
        """Fully reset the game, including legs and sets"""
        self.home.legs = self.home.sets = 0
        self.away.legs = self.away.sets = 0
        self.home.reset_for_new_leg(self.mode)
        self.away.reset_for_new_leg(self.mode)
        self.active_player = self.home  # Home throws first
        return "MATCH_RESET"

    def checkout_recs(self, remaining: int) -> str | None:
        """Suggest checkouts based on remaining score"""
        return CHECKOUTS.get(remaining)

    def process_turn(self, score: int) -> str | tuple | None:
        """Main game loop for entering a score"""
        if score > 180:
            return "SCORE_ERROR"
        self.active_player.add_score(score)

        # check for bust score
        if self.active_player.remaining == 1 or self.active_player.remaining < 0:
            prev_score = self.active_player.scores_this_leg.pop()
            self.active_player.remaining += prev_score
            self.switch_turn()
            return "BUST"

        # Check if the player won the leg
        elif self.active_player.remaining == 0:
            self.active_player.legs += 1

            # check for set win
            if self.active_player.legs == 3:
                self.active_player.sets += 1
                self.home.legs = 0
                self.away.legs = 0

                # check for match win
                if self.active_player.sets == (self.format + 1) // 2:
                    winner = self.active_player
                    self.reset_match()
                    return "PLAYER_MATCH_WIN", winner

            # set up new leg
            self.home.reset_for_new_leg(self.mode)
            self.away.reset_for_new_leg(self.mode)
            self.leg_starter = self.away if self.leg_starter == self.home else self.home
            self.active_player = self.leg_starter
            return "PLAYER_LEG_WIN"
        else:
            self.switch_turn()

    # --- History & Undo ---
    def recall(self):
        """show list of scores from both players of recent leg"""
        # Example of how you can access the data now:
        df = pd.DataFrame({
            "Home": pd.Series(self.home.scores_this_leg),
            "Away": pd.Series(self.away.scores_this_leg)
        })
        df.columns.name = "Throw"
        return df

    def error(self):
        """Undo the last score entry"""
        # get the last added score from the prev active player if it exists
        if self.non_active_player.scores_this_leg:
            prev_score = self.non_active_player.scores_this_leg.pop()
            self.non_active_player.remaining += prev_score
            self.non_active_player.throws -= 1
            # switch to the prev active player, to be able to enter the correct
            # score
            self.switch_turn()
        else:
            return "UNDO_NOT_AVAILABLE"


if __name__ == "__main__":
    # Quick test of the logic
    game = GameLogic()
    game.process_turn(100)
    game.process_turn(50)
    print(
        f"Home Remaining: {
            game.home.remaining}, Avg: {
            game.home.get_average()}")
    print(
        f"Away Remaining: {
            game.away.remaining}, Avg: {
            game.away.get_average()}")
    game.process_turn(100)
    game.process_turn(50)
    print(
        f"Home Remaining: {
            game.home.remaining}, Avg: {
            game.home.get_average()}")
    print(
        f"Away Remaining: {
            game.away.remaining}, Avg: {
            game.away.get_average()}")
    print(game.recall())
    game.process_turn(100)
    game.process_turn(50)
    game.process_turn(100)
    game.process_turn(50)
    print(
        f"Home Remaining: {
            game.home.remaining}, Avg: {
            game.home.get_average()}")
    print(
        f"Away Remaining: {
            game.away.remaining}, Avg: {
            game.away.get_average()}")
    game.process_turn(100)
    game.process_turn(180)
    print(
        f"Home Remaining: {
            game.home.remaining}, Avg: {
            game.home.get_average()}")
    print(
        f"Away Remaining: {
            game.away.remaining}, Avg: {
            game.away.get_average()}")
    print(game.checkout_recs(game.home.remaining))
    print(game.checkout_recs(game.away.remaining))
    game.error()
    game.error()
    print(
        f"Home Remaining: {
            game.home.remaining}, Avg: {
            game.home.get_average()}")
    print(
        f"Away Remaining: {
            game.away.remaining}, Avg: {
            game.away.get_average()}")
    print(game.checkout_recs(game.home.remaining))
    print(game.checkout_recs(game.away.remaining))
