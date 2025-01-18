class Board:
    # The Board class represents a Sudoku board and provides methods for solving the puzzle.

    def __init__(self, board):
        # Initializes the board with a 2D list (9x9 grid) representing the Sudoku puzzle.
        # Cells with the value 0 are considered empty.
        self.board = board

    def __str__(self):
        # Converts the board into a human-readable string format for display.
        # Replaces empty cells (0) with '*' for clarity.
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)  # Joins row values with spaces
            board_str += '\n'  # Adds a newline after each row
        return board_str

    def find_empty_cell(self):
        # Finds the first empty cell (value 0) in the board.
        # Returns a tuple (row, col) of the cell's coordinates or None if no empty cell is found.
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)  # Looks for the first occurrence of 0 in the row
                return row, col  # Returns the coordinates of the empty cell
            except ValueError:
                pass  # Moves to the next row if 0 is not found
        return None

    def valid_in_row(self, row, num):
        # Checks if a number is not already present in the specified row.
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Checks if a number is not already present in the specified column.
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        # Checks if a number is not already present in the 3x3 subgrid containing the cell (row, col).
        row_start = (row // 3) * 3  # Calculates the starting row of the 3x3 subgrid
        col_start = (col // 3) * 3  # Calculates the starting column of the 3x3 subgrid
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:  # Checks if the number is already in the subgrid
                    return False
        return True

    def is_valid(self, empty, num):
        # Checks if placing a number in the given empty cell (row, col) is valid.
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)  # Validates the row
        valid_in_col = self.valid_in_col(col, num)  # Validates the column
        valid_in_square = self.valid_in_square(row, col, num)  # Validates the 3x3 subgrid
        return all([valid_in_row, valid_in_col, valid_in_square])  # Returns True if all validations pass

    def solver(self):
        # Solves the Sudoku puzzle using backtracking.
        if (next_empty := self.find_empty_cell()) is None:
            # If there are no empty cells, the puzzle is solved.
            return True
        for guess in range(1, 10):
            # Tries each number from 1 to 9 as a candidate for the empty cell.
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess  # Temporarily places the number on the board
                if self.solver():
                    # Recursively attempts to solve the rest of the puzzle.
                    return True
                self.board[row][col] = 0  # Resets the cell if the guess leads to a dead end
        return False  # Returns False if no number can be placed in the empty cell

def solve_sudoku(board):
    # Initializes the board, prints the initial puzzle, and attempts to solve it.
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')  # Displays the unsolved puzzle
    if gameboard.solver():
        # If the puzzle is solvable, prints the solved puzzle.
        print(f'Solved puzzle:\n{gameboard}')
    else:
        # Prints a message if the puzzle is unsolvable.
        print('The provided puzzle is unsolvable.')
    return gameboard  # Returns the solved or partially solved board

# Example puzzle to solve (0 represents empty cells).
puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]