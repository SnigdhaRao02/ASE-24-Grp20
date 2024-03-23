from csv_input import csv
from row import Row
from cols import Cols
import random
import config
import math
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
    def div(self,cols=None):    
        u = {}
        m = {**self.cols.x, **self.cols.y} if cols is None else cols
        u[".N"] = len(self.rows)-1
        for _,col in m.items():
            u[col.txt] = round(col.div(),2)
        return Row(u)

    
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
    def clone(self,rows=None):
        new=Data([self.cols.names])
        for row in (rows or []):
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
        
        #function l.rnd(n, ndecs)
    #if type(n) ~= "number" then return n end
    #if math.floor(n) == n  then return n end
    ##local mult = 10^(ndecs or 2)
    #return math.floor(n * mult + 0.5) / mult end
                
        def show(self,maxDepth=0):
            # def rnd(n, ndecs=None):
            #     if not isinstance(n, (int, float)):
            #         return n
            #     if n == math.floor(n):
            #         return n
            #     mult = 10 ** (ndecs if ndecs is not None else 2)
            #     return math.floor(n * mult + 0.5) / mult
            # def distance2heaven(data):
            #     return rnd(data.mid().distance2heaven(self.here))
            # maxDepth=0
            def _show(node,depth,leafp):
                post=""
              #  nonlocal maxDepth
                #post=(distance2heaven(node.here)+"\t"+node.here.mid().cells) if leafp else ""
                if leafp:
                    post=f"\t{str(node.here.mid().cells)}"
                   # print("POST!!!", )
                nonlocal maxDepth
                maxDepth=max(maxDepth,depth)
                print(('|.. ' * depth) + post)
                
            self.walk(_show)
            print("")
            #print("ss",self.here.mid().cells)
            print("    " * maxDepth, str(self.here.mid().cells))
            print("    " * maxDepth, "_", str(self.here.cols.names))
            #print(("   ") * maxDepth,distance2heaven(self.here),self.here.mid().cells)
            #print(("  ") * maxDepth,"-",self.here.cols.names)
    def farapart(self,rows,sortp,a=None):
        far = int((len(rows)-1) * config.the.Far)
        evals = 1 if a else 2
        a = random.choice(rows)
        a_neighbors = sorted(a.neighbors(self), key=lambda row: row.distance2heaven(self))
        b = a_neighbors[far]

        if sortp and b.distance2heaven(self) < a.distance2heaven(self):
            a, b = b, a

        return a, b, a.dist(b, self), evals
        # far=int((len(rows)*config.the.Far)//1)
        # #far=int((len(rows)-1)*config.the.Far) 
        # evals=1 if a else 2
        # a=a or random.choice(rows).neighbors(self,rows)[far]
        
        # b=a.neighbors(self,rows)[far]
        # if sortp and b.distance2heaven(self)<a.distance2heaven(self):
        #     a,b=b,a
        # return a,b,a.dist(b,self),evals 
    #should write half and tree functions 

    #function l.many(t,  n,     u)
    #n = n or #t
    #u={}; for _ = 1,n do u[1+#u] = l.any(t) end; return u end

    def half(self,rows,sortp,before=None):
       
        some=random.sample(rows,min(config.the.Half,len(rows)))
        #some  = l.many(rows, math.min(the.Half,#rows))
        # n=min(config.the.Half,len(rows)) or len(rows)
       
        # for i in range(n):
        #     #t[math.random(#t)]
        #     some.append(random.choice(rows))
           # some.append(rows[random.randint(0,len(rows)-1)])
        a,b,C,evals=self.farapart(some,sortp,before)
        aas=[]
        bs=[]
        # def d(row1,row2):
        #     return row1.dist(row2,self)
        def project(r):
            return (r.dist( a,self ) **2+ (C ** 2) - (r.dist( b,self )**2))/(2 *C )
        #l.keysort
        def keysort(t,fun):
            u=[{'x':x,'y':fun(x)} for x in t]
            u.sort(key=lambda a: a['y'])
            v=[xy['x'] for xy in u]
            print(v)
            return v
        #sorted(rows_to_sort, key=lambda row: self.dist(row, data)
        # sorted(rows key=lambda row: project)
        rows=rows[1:]
        sorted_rows=sorted(rows,key=project)
        m=len(rows)//2 
        aas,bs=sorted_rows[:m],sorted_rows[m:]
        # for n,row in enumerate(sorted(rows, key=lambda row: project(row)),1):
        #     if n<=len(rows)//2:
        #         aas.append(row)
        #     else:
        #         bs.append(row)
        return aas,bs,a,b,C,a.dist(bs[0],self),evals
    
    #tree function
    def tree(self,sortp):
        evals=0
        def _tree(data,above=None):
            nonlocal evals
            node=Data.Node(data)
            if(len(data.rows)> 2*math.sqrt(len(self.rows))):
                lefts,rights,node.lefts,node.rights,node.C,node.cut,evals1=data.half(data.rows,sortp,above)
                evals+=evals1
                node.lefts=_tree(data.clone(lefts))
                node.rights=_tree(data.clone(rights))
            return node
        return _tree(self),evals
    
    def branch(self,stop=None):
        evals=1
        rest=[]
        stop=stop or (2*(len(self.rows)**0.5))
        def _branch(data,above=None):
            nonlocal evals
            if len(data.rows)>stop:
                lefts,rights,left,a,b,c,d=self.half(data.rows[1:],True,above)
                evals = evals+1 
                
                
                for _,row1 in enumerate(rights):
                    rest.append(row1)
                return _branch(data.clone(lefts),left)
            else:
                return data.clone(data.rows[1:]), data.clone(rest), evals
            
        return _branch(self)





            

            















      


        