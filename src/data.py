from csv_input import csv
from row import Row
from cols import Cols
import random
class Data:
    
    def __init__(self,src,fun=None) -> None:
        self.rows=[]
        self.cols=None
        if(isinstance(src,str)):
            reader=csv(src)
            for row in reader:
                self.add(Row(row),fun)
                # print(row)
        else:
            self.add(Row(src),fun)
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

    def gate(self, budget0, budget, some):
        rows, lite, dark=None, None, None
        stats, bests ={},{}
        rows=self.rows
        random.shuffle(rows)
        lite=rows[:budget0+1]
        dark=rows[budget0+1:]
        for i in range(1,budget+1): # Since we need to include budget and range does not include second number
            best, rest = self.bestRest(lite, pow(len(lite),some))
            todo, selected = self.split(best, rest, lite, dark)
            stats[i]=selected.mid()
            bests[i]=best.rows[0]
            lite.append(todo)
            dark.remove(todo)
        return {stats,bests}
    

    def split(self, best, rest, lite, dark):
        selected, max, out =None, None, None
        selected= Data(self.cols.names)
        max=1000000000000000
        out=0
        for i,row in dark.items():
            b,r,tmp=None
            b=row.like(best,len(lite),2)
            r=row.like(rest,len(lite),2)
            if(b>r):
                selected.append(row)
            tmp= abs(b+r) / abs(b-r+ pow(10,-300))
            if(tmp>max):
                out,max=i,tmp
        return {out,selected}
    
    def bestRest(self,rows, want):
        rows.sort(key=lambda a: a.distance2heaven())
        best, rest=list(self.cols.names), list(self.cols.names)
        for i, row in rows.items():
            if(i<=want):
                best.append(row)
            else:
                rest.append(row)
        return Data(best), Data(rest)












      


        