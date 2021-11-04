class ChessBoard:
    def __init__(self):
        self.figures = {}

    def __add__(self, namewage):
        name = namewage[0]
        wage = namewage[1]
        if wage in [1, 3, 4, 5, 10, 999]:
            new_figure = Pawn(name, wage)
            self.figures[name] = new_figure
        else:
            print(f'Sorry, wrong walue! Cannot add {name} to the chess board.')

    def __lt__(self, a):
        f = {}
        for a, b in self.figures.items():
            f[a] = b.wage
        f = sorted(f.items(), key=lambda f: f[1])
        print('Posortowane figury:')
        for x in f:
            print(x[0])




class Pawn:
    def __init__(self, name, wage):
        self.name = name
        self.wage = wage
        self.settype()

    def settype(self):
        if self.wage == 1:
            self.type = "Pionek"
        elif self.wage == 3:
            self.type = "Kon"
        elif self.wage == 4:
            self.type = "Goniec"
        elif self.wage == 5:
            self.type = "Wieza"
        elif self.wage == 10:
            self.type = "Hetman"
        elif self.wage == 999:
            self.type = "Krol"


a = ChessBoard()

a + ["pionek1", 1]                      # adds new figure
a + ["pionek2", 1]
a + ["kon1", 3]
a + ["krol", 999]
a + ['glupi goniec 27', 666]
a < 4                                   # compares figures wages and displays a list of sorted figures