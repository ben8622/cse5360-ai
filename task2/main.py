from classes.GameState import GameState
from classes.Action import Action
import sys


def main():
    # extract command line args
    mode: str = sys.argv[1]
    input_file: str = sys.argv[2]
    output_file: str = sys.argv[3]
    depth: int = int(sys.argv[4])

    # init starting game state
    start: GameState = GameState()

    # parse file contents into game state
    with open(input_file) as f:
        for line in f.readlines():
            # reached EOF strip last line of '\n' and store
            if len(line) == 2:
                start.next = line.strip()
                break

            # strip '\n' and parse into list
            row = list(line)
            row.pop()
            start.playing_board.append(row)

    print(start.print_board())




    return


if __name__ == "__main__":
    main()
