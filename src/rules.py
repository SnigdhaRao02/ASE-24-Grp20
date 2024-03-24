import config2
from itertools import chain, combinations
import rule as Rule


class Rules:
    
    def __init__(self, ranges, goal, rowss) -> None:
        print("Creating instance of Rules")
        for _, row in rowss.items():
            print(_, " ", len(row), "items")
        self.sorted={}
        self.goal=goal
        self.rowss=rowss
        self.LIKE=0
        self.HATE=0

        self.likeHate()
        for _, range in ranges.items():
            range.scored= self.score(range.y)
        self.sorted = self.top(self._try( self.top(ranges)))
    def top(self,t):
        t.sort(key=lambda x: x.scored, reverse=True)
        u=[]
        for _,x in t.items():
            if x.scored>=t[1].scored * config2.the.Cut:
                u.append(x)
        return u[:config2.the.Beam+1]



    
    def likeHate(self):
        for y, rows in self.rowss.items():
            if y == self.goal:
                self.LIKE += len(rows)
            else:
                self.HATE+= len(rows)
    
    def score(self, goal, LIKE, HATE):
        like, hate, tiny = 0,0,pow(1,-30)
        for klass,n in self.y.items():
            if klass == goal:
                like+= n 
            else:
                hate+=n
        like, hate= like/ (LIKE + tiny), hate/ (HATE + tiny)
        if hate > like:
            return 0
        else:
            return (pow(like, config2.the.Support) / (like + hate))
        
    def powerset(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))


    def _try(self, ranges):
        u=[]
        for _, subset in self.powerset(ranges).items():
            if len(subset) >0:
                rule = Rule.new(subset)
                rule.scored=self.score(rule.selects(self.rowss))
                if rule.scored >0.01:
                    u.append(rule)
        return u
