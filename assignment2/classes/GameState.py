class GameState:
    def __init__(self):
        self.score_player: int = 0
        self.score_opponent: int = 0
        self.next: str = "1"
        self.playing_board: list[int] = []

    def count_score(self):
        return

    def print_score(self):
        print("PLAYER | OPPONENT")
        print(f"{self.score_player}      | {self.score_opponent}")

    def print_board(self):
        for l in self.playing_board:
            print(l)
