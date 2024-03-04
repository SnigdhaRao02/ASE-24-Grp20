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

