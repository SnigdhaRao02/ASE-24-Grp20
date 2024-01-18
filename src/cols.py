import re
from num import Num
from sym import Sym
from row import Row

class Cols:
    def __init__ (self, row):
        self.x={}
        self.y={}
        self.all = {}
        self.klass=None
        self.names= row

        for name_col in row:
            n= row.index(name_col)
            name_col = name_col.strip()
            if name_col[0].islower():
                col = Sym(name_col,n)
                
                
            else:
                col = Num(name_col, n)
            self.all[n]=col
            if not name_col[-1] == "X":
                if "!" in name_col:
                    self.klass =col
                if re.findall("[!+-]$", name_col):
                    self.y[n]=col
                else:
                    self.x[n]=col

    def add(self, row):
        for col in self.y:
            col.add(row[col.at])
        for col in self.x:
            col.add(row[col.at])
        
        #for A in [self.x, self.y]:
            #for col in A:
                #col.add(row.cells[col.at])
        #return row
    
    

c1=Cols(["a","B","cX"])
#c1.add([1,2,3])