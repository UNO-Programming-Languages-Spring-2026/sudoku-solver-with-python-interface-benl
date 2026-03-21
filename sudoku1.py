import sys, clingo


class ClingoApp(clingo.application.Application):

    def print_model(self, model, printer) -> None:
        symbols = sorted(model.symbols(shown=True))
        print(" ".join(str(s) for s in symbols))
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