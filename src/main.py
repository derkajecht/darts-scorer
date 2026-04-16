"""Backend logic for the scorer"""

from gui import DartsApp


def main() -> int:
    app = DartsApp()
    app.run()
    return 0


if __name__ == "__main__":
    main()
