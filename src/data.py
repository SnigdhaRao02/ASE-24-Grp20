from csv_input import get_csv_rows
from row import Row
from cols import Cols
class Data:
    def __init__(self,src,fun) -> None:
        self.rows={}
        self.cols=None
        if(isinstance(src,str)):
            for row in get_csv_rows():
                self.add(row,fun)
        else:
            for row in fun:
                self.add(row,fun)


    def add(self,t,fun,row):
        row=Row(t)
        if(self.cols!=None):
            self.rows.append(row)
            self.cols.add(row)
        else:
            self.cols=Cols(row)
   # def mid(self,cols, u):


  #  def div(self,cols, u):
    
#    def stats(self,cols,fun,ndivs,u):
  #      u={".N":len(self.rows)}
   #     for col in self.cols[cols or "y"]:







      


        