from csv_input import csv
from row import Row
from cols import Cols
class Data:
    
    def __init__(self,src,fun=None) -> None:
        self.rows=[]
        self.cols=None
        if(isinstance(src,str)):
            reader=csv(src)
            for row in reader:
                self.add(row,fun)
                # print(row)
       # else:
        #   for _,row in enumerate(src):
                # self.add(row,fun)
                # print(row,"YAYAYA")


    def add(self,t,fun=None):
        # if(t.cells!=None):
        #     row=t
        # else:

        row = t if type(t) == Row else Row(t)
        #row=Row(t)
        #row = t.cells if t.cells else ROW.new(t)
        if(self.cols!=None):  
            if(fun!=None):
                fun(self,row)    
            # self.cols.add(row.cells)
            self.rows.append(self.cols.add(row.cells))
        else:
            self.cols=Cols(row.cells)
        #self.rows.append(row.cells)

    def mid(self, cols=None):
        # Calculate the mid (mean/mode) of the specified columns
        u = {}
        m = {**self.cols.x, **self.cols.y} if cols is None else cols
        u[".N"] = len(self.rows)-1
        for _,col in m.items():
            u[col.txt] = col.mid()
        return Row(u)
    

   # def mid(self,cols, u):


  #  def div(self,cols, u):
    
#    def stats(self,cols,fun,ndivs,u):
  #      u={".N":len(self.rows)}
   #     for col in self.cols[cols or "y"]:







      


        