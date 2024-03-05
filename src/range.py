import config2
import math
class Range:

    def __init__(self, at, txt, lo, hi=None) -> None:
        self.at = at
        self.txt = txt
        self.x= { "lo": lo, "hi": hi or lo}
        self.y = {}

    def add(self, x ,y):
        self.x["lo"]= min(self.x["lo"], x)
        self.x["hi"]= max(self.x["hi"], x)
        if self.y.get(y, 0): 
            self.y[y] = self.y[y] + 1
        else:
            self.y[y] = 1

    def show(self):
        lo,hi,s = self.x["lo"], self.x["hi"],self.txt
        if lo == -math.inf:
            return str(s)+" < "+ str(hi)
        if hi == math.inf:
            return str(s)+" >= "+ str(lo)
        if lo == hi:
            return(str(s) + " == " + str(lo))
        return (str(lo) + " <= " + s + " < " + str(hi))
    
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
    
    def merge(self,other):
        both=Range(self.at,self.txt,self.x["lo"])
        both.x["lo"]=min(self.x["lo"],other.x["lo"])
        both.x["hi"]=max(self.x["hi"],other.x["hi"])
        for _,t in enumerate(self.y,other.y):
            for k,v in t.items():
                both.y[k]=both.y.get(k,0)+v
        return both
    
    def merged(self,other,tooFew):
        def entropy(t):
            n,e=0,0
            for _,v in t.items():
                n+=v
            for _,v in t.items():
                e=e-v/n * math.log(v/n,2)
            return e,n
        both=self.merge(other)
        e1,n1=entropy(self.y)
        e2,n2=entropy(other.y)
        if n1<=tooFew or n2<=tooFew:
            return both
        if entropy(both.y) <= (n1*e1 + n2*e2)/(n1+n2):
            return both

