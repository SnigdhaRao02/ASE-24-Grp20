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
            for row in (src or []):
               
                self.add(Row(row),fun)

               # print("row",row)
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
        if(self.cols is None):
            self.cols=Cols(row.cells)
        else:
            if(fun is not None):
                fun(self,row)
            
            self.cols.add(row)
           
        self.rows.append(row)

        # if(self.cols!=None):  
        #     if(fun!=None):
        #         fun(self,row)
        #     print("error:",row.cells)
        #     self.cols.add(row)    
        #     # self.cols.add(row.cells)
            
        # else:
        #     self.cols=Cols(row.cells)
        # self.rows.append(row)
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

    def gate(self, budget0, budget, some,ans):
        #print('entered gate')
        rows = random.sample(self.rows[1:], len(self.rows)-1)
        ans[0].append("1. top 6 \n" + str([top6.cells[5:8] for top6 in rows[:6]]))
        ans[1].append("2. top 50 \n " + str([top50.cells[5:8] for top50 in rows[:50]]))
       # print("2. top50",top6)

        
        
        rows.sort(key=lambda x: x.distance2heaven(self))
        ans[2].append("3. most \n"+str((rows[0].cells)[5:]))
        
        
        rows = random.sample(self.rows[1:], len(self.rows)-1)
        stats, bests =[],[]
        #rows=self.rows
        #random.shuffle(rows)
        lite=rows[:budget0]
        dark=rows[budget0:]
        for i in range(budget): # Since we need to include budget and range does not include second number
            best, rest = self.bestRest(lite, len(lite) ** some)
            
            todo, selected = self.split(best, rest, lite, dark)
            ans[3].append("4: rand \n " + str(self.get_centroid(random.sample(dark,budget0+i), 5, 8)))
            ans[4].append("5: mid \n " + str(self.get_centroid(selected.rows[1:], 5, 8)))
            ans[5].append("6: top: \n " + str(best.rows[1].cells[5:8]))
           # print("stats append",selected.mid().cells)
            stats.append(selected.mid())
            
            bests.append(best.rows[1])
            lite.append(dark.pop(todo))
            
        return stats,bests
    

    def split(self, best, rest, lite, dark):
        selected, max, out =None, None, None
        selected= Data([self.cols.names])
        max=1E30
        out=1
        for i,row in enumerate(dark):
           # b,r,tmp=None,None,None
            b=row.like(best,len(lite),2)
            r=row.like(rest,len(lite),2)
            #print(b,r,row.cells)
            if(b>r):
                #print("selected row",row.cells)
                selected.add(row)
            tmp= abs(b+r) / abs(b-r+ pow(10,-300))
            if(tmp>max):
                out,max=i,tmp
        return out,selected  
    
    def bestRest(self,rows, want):
        rows.sort(key=lambda a: a.distance2heaven(self))
       
        best, rest=[self.cols.names], [self.cols.names]
       
        for i, row in enumerate(rows):
            if(i<want):
                best.append(row.cells)
            else:
                rest.append(row.cells)
           
        return Data(best), Data(rest)
    def get_centroid(self, rows, i, j):
        centroid = []
        for k in range(i,j):
            centroid.append(0)
        for row in rows:
            y = row.cells[i:j]
            centroid = [sum(k) for k in zip(y, centroid)]
        for k in range(len(centroid)):
            if(len(rows)!=0):
                centroid[k]/=len(rows)
        return centroid












      


        