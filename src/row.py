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
        for _,col in data.cols.y.items():
            n+=1
            d+=pow(abs(col.heaven - col.norm(self.cells[col.at])),2)
        return pow(d,0.5)/ pow(n,0.5)


