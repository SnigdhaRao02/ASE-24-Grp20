import re
from num import Num
from sym import Sym

class Cols:
    def __init__ (self, row):
        self.x=[]
        self.y=[]
        self.all = []
        self.klass=None
        self.names= row

        for name_col in row:
            n= row.index(name_col)
            name_col = name_col.strip()
            if name_col[0].islower():
                col = Sym(name_col,n)
            else:
                col = Num(name_col, n)
            self.all.append(col)
            if not name_col[-1] == "X":
                if "!" in name_col:
                    self.klass =col
                if re.findall("[!+-]$", name_col):
                    self.y.append(col)
                else:
                    self.x.append(col)

def add(self, row):
        for A in [self.x, self.y]:
            for col in A:
                col.add(row.cells[col.at])
