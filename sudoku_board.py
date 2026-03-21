from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        rows = []
        for x in range(9):
            column = []
            for y in range(9):
                column.append(0)
            rows.append(column)
        for key in self.sudoku:
            x = key[0] - 1
            y = key[1] - 1
            v = self.sudoku[key]
            rows[x][y] = v
        for i in range(len(rows)):
            s = s + "{0} {1} {2}  {3} {4} {5}  {6} {7} {8}\n".format(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7], rows[i][8])
            if ((i + 1) % 3 == 0) and ((i + 1) < len(rows)):
                s = s + "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        digits = "-0123456789"
        start = 0
        end = 0
        position = -1
        mode = 0
        for i in range(len(s)):
            if mode == 0:
                start = i
                if s[start] in digits:
                    end = start
                    position += 1
                    mode = 1
            else:
                end = i
                if s[end] not in digits:
                    if s[start] != '-':
                        sudoku[((position // 9) + 1, (position % 9) + 1)] = int(s[start:end])
                    mode = 0
        if mode == 1:
            if s[start] != '-':
                sudoku[((position // 9) + 1, (position % 9) + 1)] = int(s[start:(end + 1)])
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        sudokusymbols = model.symbols(shown=True)
        sudokustrings = [str(s) for s in sudokusymbols]
        start = 0
        while True:
            if sudokustrings[0][start] == '(':
                start += 1
                break
            else:
                start += 1
        digits = "0123456789"
        for i in range(len(sudokustrings)):
            left = start
            right = 0
            while True:
                if sudokustrings[i][left + right] not in digits:
                    break
                else:
                    right += 1
            row = int(sudokustrings[i][left:(left + right)])
            left = left + right + 1
            right = 0
            while True:
                if sudokustrings[i][left + right] not in digits:
                    break
                else:
                    right += 1
            column = int(sudokustrings[i][left:(left + right)])
            left = left + right + 1
            right = 0
            while True:
                if sudokustrings[i][left + right] not in digits:
                    break
                else:
                    right += 1
            value = int(sudokustrings[i][left:(left + right)])
            sudoku[(row, column)] = value
        return cls(sudoku)
