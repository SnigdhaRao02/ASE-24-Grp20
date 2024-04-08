import config2
from itertools import chain, combinations

import config2

class Rule:
    
    def __init__(self, ranges) -> None:
        self.parts={}
        self.scored=0
        for range in ranges:
            self.parts.setdefault(range.txt, []).append(range)
       
        # for range in ranges:
        #     #print('txt', range.txt)
        #     if( range.txt in self.parts):
        #         t=self.parts[range.txt]
        #     else:
        #         t=[]
            
        #     t.append(range)
        #     self.parts[range.txt]=t 
       
    def selects(self,rows):
        t=[]
       # print("select rows", rows)
        for r in rows:
            if self._and(r):
                t.append(r)
        return t
    def selectss(self,rowss):
        t={}
        #print("rowss",rowss)
        for y,rows in rowss.items():
            t[y]=len(self.selects(rows))
        return t
    def _and(self,row):
        for ranges in self.parts.values():
            if not self._or(ranges,row):
                return False 
        return True 
    def _or(self,ranges,row):
        ##print("ranges[1]"," ",ranges[0].at)
        #print("rule", row[0].cells, row[1].cells)
       
        x=row.cells[ranges[0].at]
        if x=="?":
            return True 
        for range in ranges:
            lo,hi=range.x["lo"],range.x["hi"] 
            if (lo==hi and lo==x) or (lo<=x and x<hi):
                return True 
        return False 
    
    def show(self):
        ands=[]
        for ranges in self.parts.values():
            ors=_showless(ranges) 
            print("ors",ors)
            at=0 
            for i,range in enumerate(ors):
                at=range.at 
                ors[i]=range.show()
            ands.append(" or ".join(ors))
        print("ands",ands)
        return " and ".join(ands)
def copy(t):
    if not isinstance(t,dict):
        return t 
    u={}
    for k,v in t.items():
        u[copy(k)]=copy(v)
    return u
 
def _showless(t,ready=False):
    if not ready:
        t=copy(t)
        t.sort(key=lambda x: x.x["lo"])
    i,u=0,[]
    
    while i<len(t):
        a=t[i]
        if i<len(t)-1:
            if a.x["hi"]==t[i+1].x["lo"]:
                a=a.merge(t[i+1])
                i=i+1 
        u.append(a)
        i=i+1 
    if(len(u)==len(t)):
        return t 
    else:
        return _showless(u,ready=True)







        
    

        