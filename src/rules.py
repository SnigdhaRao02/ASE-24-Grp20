import config2
from itertools import chain, combinations
from rule import Rule


class Rules:
    
    def __init__(self, ranges, goal, rowss) -> None:
        print("Creating instance of Rules")
        for _, row in rowss.items():
            print(_, " ", len(row), "items")
        self.sorted=[]
        self.goal=goal
        self.rowss=rowss
        self.LIKE=0
        self.HATE=0

        self.likeHate()
        for _, range in enumerate(ranges):
            print("Ranges: ",range.y)
            range.scored= self.score(range.y,self.goal)
        self.sorted = self.top(self._try( self.top(ranges)))
    def top(self,t):
        t.sort(key=lambda x: x.scored, reverse=True)
        u=[]
        for _,x in enumerate(t):
            if x.scored>=t[0].scored * config2.the.Cut:
                u.append(x)
       # print("top", u)
        return u[:config2.the.Beam+1]



    
    def likeHate(self):
        for y, rows in self.rowss.items():
            if y == self.goal:
                self.LIKE += len(rows)
            else:
                self.HATE+= len(rows)
    
    def score(self, t,goal):
        print("t"," ",t)
        like, hate, tiny = 0,0,pow(1,-30)
        for klass,n in t.items():
            if klass == goal:
                like+= n 
            else:
                hate+=n
        print(like,hate)
        like, hate= like/ (self.LIKE + tiny), hate/ (self.HATE + tiny)
        
        if hate >=like:
            return 0
        else:
            return (pow(like, config2.the.Support) / (like + hate))
        
    def powerset(self,iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(1,len(s)+1))


    def _try(self, ranges):
        u=[]
        for _, subset in enumerate(self.powerset(ranges)):
            #print("subset",subset)
            if len(subset) >0:
                rule = Rule(subset)
                rule.scored=self.score(rule.selectss(self.rowss),self.goal)
                if rule.scored >0.01:
                    u.append(rule)
        return u
