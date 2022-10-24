from .GameState import GameState


class Action:
    def __init__(self):
        self.coordinates: tuple[int, int] = ()
        self.players_move: bool = True

        self.prev_state: GameState = GameState()
        self.curr_state: GameState = GameState()

        self.prev_actions: Action = Action()
        self.possible_actions: list[Action] = []

        self.score: int = 0
