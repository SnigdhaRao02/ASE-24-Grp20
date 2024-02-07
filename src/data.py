from csv_input import csv
from row import Row
from cols import Cols
import random
import config
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
    def clone(self,rows):
        new=Data(self.cols.names)
        for _,row in rows.items():
            new.add(row)
        return new 
    class Node:
        def __init__(self,data):
            self.here=data 
            self.lefts=None
            self.rights=None
            self.C=None
            self.cut=None
        def walk(self,fun,depth=0):
            fun(self,depth,not (self.lefts or self.rights))
            if self.lefts:
                self.lefts.walk(fun,depth+1)
            if self.rights:
                self.rights.walk(fun,depth+1)
        def show(self,_show):
            def distance2heaven(data):
                return data.mid().distance2heaven(self.here)
            maxDepth=0
            def _show(node,depth,leafp):
                post=(distance2heaven(node.here)+"\t"+node.here.mid().cells) if leafp else ""
                maxDepth=max(maxDepth,depth)
                print(('|.. ' * depth) + post)
            self.walk(_show)
            print(("   ") * maxDepth,distance2heaven(self.here),self.here.mid().cells)
            print(("  ") * maxDepth,"-",self.here.cols.names)
    def farapart(self,rows,sortp,a,b):
        far=(len(rows)*config.the.Far)//1
        evals=1 if a else 2
        a=a or self.random.choice(rows).neighbors(self,rows)[far]
        b=a.neighbors(self,rows)[far]
        if sortp and b.distance2heaven(self)<a.distance2heaven(self):
            a,b=b,a
        return a,b,a.dist(b,self),evals 
    #should write half and tree functions 

    #function l.many(t,  n,     u)
    #n = n or #t
    #u={}; for _ = 1,n do u[1+#u] = l.any(t) end; return u end

    def half(self,rows,sortp,before):
        some,a,b,d,C,project,aas,bs=[],None,None,None,None,None,[],[]
        n=min(config.the.Half,len(rows))
        for i in range(n):
            some.append(self.random.choice(rows))
        a,b,C,evals=self.farapart(some,sortp,before)
        def d(row1,row2):
            return row1.dist(row2,self)
        def project(r):
            return (pow(d(r,a),2)+pow(C,2) - pow(d(r,b),2))/(2*C)
        #l.keysort
        def keysort(t,fun):
            u=[{'x':x,'y':fun(x)} for x in t]
            u.sort(key=lambda a: a['y'])
            v=[xy['x'] for xy in u]
            return v
        for n,row in enumerate(keysort(rows,project),1):
            if n<=len(rows)//2:
                aas.append(row)
            else:
                bs.append(row)
        return aas,bs,a,b,C,d(a,bs[1]),evals
    
    #tree function
    def tree(self,sortp):
        evals=0
        def _tree(data,above):
            node=Data.Node(data)
            if(len(data.rows)> 2*(len(self.rows)**0.5)):
                lefts,rights,node.lefts,node.rights,node.C,node.cut,evals1=self.half(data.rows,sortp,above)
                evals=evals+evals1
                node.lefts=_tree(self.clone(lefts),node.lefts)
                node.rights=_tree(self.clone(rights),node.rights)
            return node
        return _tree(self),evals




            

            















      


        