import config2
from itertools import chain, combinations

import config2

class Rule:
    
    def __init__(self, ranges) -> None:
        self.parts={}
        self.scored=0
        for _, range in ranges.items():
            t=(self.parts[range.txt] or {})
            t.append(range)
            self.parts[range.txt]=t 
        return self
    def selects(self,rows):
        t=[]
        for _,r in rows.items():
            if self._and(r):
                t.append(r)
        return t
    def _and(self,row):
        for _,ranges in (self.parts).items():
            if not self._or(ranges,row):
                return False 
        return True 
    def _or(self,ranges,row):
        x=row.cells[ranges[1].at]
        if x=="?":
            return True 
        for _,range in ranges.items():
            lo,hi=range.x.lo,range.x.hi 
            if (lo==hi and lo==x) or (lo<=x and x<hi):
                return True 
        return False 
    
    def show(self):
        ands=[]
        for _,ranges in (self.parts).items():
            ors=_showless(ranges) 
            at=0 
            for i,range in enumerate(ors):
                at=range.at 
                ors[i]=range.show()
            ands.append(" or ".join(ors))
        return " and ".join(ands) 
def _showless(t,ready=None):
    if not ready:
        t=t 
        t.sort(key=lambda x: x.lo)
    i,u=1,[]
    
    while i<= len(t):
        a=t[i]
        if i<len(t):
            if a.x.hi==t[i+1].x.lo:
                a=a.merge(t[i+1])
                i=i+1 
        u.append(a)
        i=i+1 
    if(len(u)==len(t)):
        return t 
    else:
        return _showless(u,ready)







        
    

        