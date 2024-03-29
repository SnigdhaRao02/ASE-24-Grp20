import config
import math

class Row:
    def __init__(self,t):
        self.cells=t
    
    #Part of HW3
        
    def like(self,data,n,nHypotheses):
        prior= (len(data.rows) + config.the.k) / (n + config.the.k * nHypotheses)
        out= math.log(prior)
        for _,col in data.cols.x.items():
           
            v=self.cells[col.at]
            
           
            if v != "?":
                inc=col.like(v,prior)
                if(inc!=0):
                    out=out + math.log(inc)
        return math.exp(out)
    # datas is dictionary
    def likes(self,datas,most=None):
        n,nHypotheses=0,0
        for k,data in datas.items():
            n+= len(data.rows)
            nHypotheses+=1
        for k,data in datas.items():
            temp=self.like(data,n,nHypotheses)
            if most==None or temp>most:
                most=temp
                out=k
        return out,most
    
    def distance2heaven(self,data):
        d,n=0,0
       # print("a",data.cols.y[5].txt)
        for k,col in data.cols.y.items():
            
            #print("!!",k,self.cells)
            n+=1
            if(isinstance(self.cells,dict)):
                d += math.pow(math.fabs(data.cols.y[k].heaven - data.cols.y[k].norm(self.cells[data.cols.y[k].txt])), 2)
            else:
                d += math.pow(math.fabs(data.cols.y[k].heaven - data.cols.y[k].norm(self.cells[k])), 2)
            # d += math.pow(abs(col.heaven - col.norm(self.cells[col.at])), 2)
          
        return math.sqrt(d / n) if n>0 else 0
    
    # Add distance function -> dist
    def dist(self,other, data):
       # print("other",other.cells)
        d,n,p = 0,0, config.the.p # Since p is currently not present in config ( config.p)
        for _, col in data.cols.x.items():
            n+=1
         #   print("self.cells",self.cells)
            d+=math.pow(col.dist(self.cells[col.at], other.cells[col.at]), p)
            #print("d",d)
        return math.pow((d/n),(1/p))

    # Add neighbours function
    def neighbors(self, data, rows=None):
        #l.keysort
        # def keysort(t,fun):
        #     u=[{'x':x,'y':fun(x)} for x in t]
        #     u.sort(key=lambda a: a['y'])
        #     v=[xy['x'] for xy in u]
        #     print(v)
        #     return v
        # def distt(rows):
        #     for row in rows:
        #         self.dist(row)
        

        # return keysort(rows or data.rows, distt(rows or data.rows))
        if rows is None:
            rows = data.rows
        rows_to_sort= rows[1:]
      
        return sorted(rows_to_sort, key=lambda row: self.dist(row, data))


