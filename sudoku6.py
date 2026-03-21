import sys, clingo
from sudoku_board import Sudoku


class Context:
    
    def __init__(self, board: Sudoku):
        # YOUR CODE HERE
        self.__initials = []
        for key in board.sudoku:
            x = clingo.Number(key[0])
            y = clingo.Number(key[1])
            v = clingo.Number(board.sudoku[key])
            i = clingo.Tuple_((x, y, v))
            self.__initials.append(i)
    
    def initial(self) -> list[clingo.symbol.Symbol]:
        # YOUR CODE HERE
        return self.__initials


class ClingoApp(clingo.application.Application):

    def print_model(self, model, printer) -> None:
        sudoku = Sudoku.from_model(model)
        print(sudoku)
        sys.stdout.flush()
    
    def main(self, ctl, files):
        contents = ""
        for f in files:
            reference = open(f, 'r')
            contents = reference.read()
            reference.close()
        board = Sudoku.from_str(contents)
        context = Context(board)
        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")
        ctl.ground(context = context)
        ctl.solve()


clingo.application.clingo_main(ClingoApp())