import sys, clingo
from sudoku_board import Sudoku


class ClingoApp(clingo.application.Application):

    def print_model(self, model, printer) -> None:
        sudoku = Sudoku.from_model(model)
        print(sudoku)
        sys.stdout.flush()
    
    def main(self, ctl, files):
        for f in files:
            ctl.load(f)
        if not files:
            ctl.load("-")
        ctl.load("sudoku.lp")
        ctl.ground()
        ctl.solve()


clingo.application.clingo_main(ClingoApp())