# Tic-Tac-Toe (Command Line)

A simple console tic-tac-toe game written in Python. You play against the computer, which picks its moves at random.

## Rules of this version

- The computer plays **X**, and you play **O**.
- The computer always makes the first move, placing its `X` in the **middle** of the board.
- Squares are numbered **1 to 9**, row by row:

  ```
  1 | 2 | 3
  4 | 5 | 6
  7 | 8 | 9
  ```

- On your turn, enter the number of the square you want.
- The game ends when someone gets three in a row (horizontally, vertically or diagonally) or when the board is full (a tie).
- There is no AI. The computer simply picks a random free square.

## Requirements

- Python 3.6 or newer
- No external libraries (only `random` from the standard library)

## How to run

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
python tic_tac_toe.py
```

On some systems you may need to use `python3` instead of `python`.

## Example session

```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
```

Your move replaces the number with an `O`, then the computer responds with an `X`, and the board is redrawn until the game ends with one of these messages:

- `You won!`
- `The computer won!`
- `Tie!`

## How it works

The board is a list of three lists (the rows), so any square can be accessed with `board[row][column]`. A free square holds its number (1-9), and a taken square holds `'X'` or `'O'`.

To convert a square number into board coordinates:

```python
row = (number - 1) // 3
col = (number - 1) % 3
```

### Functions

| Function | Purpose |
|---|---|
| `display_board(board)` | Prints the board to the console in the required format. |
| `enter_move(board)` | Asks the user for a move, validates it (integer, 1-9, square not taken), and places an `O`. |
| `make_list_of_free_fields(board)` | Returns a list of `(row, column)` tuples for every free square. |
| `victory_for(board, sign)` | Checks the 3 rows, 3 columns and 2 diagonals to see if `sign` has won. |
| `draw_move(board)` | Picks a random free square with `randrange()` and places an `X`. |

### Game loop

1. Set up the board and place the first `X` in the middle.
2. Display the board.
3. Take the current player's move (human or computer).
4. Check for a win. If someone has won, stop.
5. Switch turns and recompute the free squares.
6. Repeat until there is a winner or no free squares remain (a tie).

## Input validation

Your move is rejected, and you are asked again, if:

- it is not a whole number,
- it is less than 1 or greater than 9,
- the chosen square is already occupied.

## Project structure

```
.
├── tic_tac_toe.py   # the whole game
└── README.md
```

## Concepts practised

- Nested lists (2D board) and list comprehensions
- Functions, parameters and return values
- Tuples and tuple unpacking
- `while` and `for` loops, `break`
- `try` / `except` for input validation
- Random numbers with `random.randrange()`

## Possible improvements

- Let the computer block the user's winning move or take its own winning move
- Let the user choose whether to go first
- Add a "play again" option
- Add unit tests for `victory_for` and `make_list_of_free_fields`
