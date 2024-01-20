class Num:
    def __init__(self,s="",n=0) -> None:
        self.at= n
        self.txt= s
        self.n=0
        self.mu = 0 #mean
        self.m2 = 0
        self.lo,self.hi =1000000000000000, -1000000000000000
        #heaven to be added
    def add(self,x):
        if x!="?":
            self.n+=1
            x=float(x)
            d=x-self.mu
            self.mu+=d/self.n
            self.m2+=d*(x-self.mu)
            self.lo=min(x,self.lo)
            self.hi=max(x,self.hi)
    def mid(self):
        return self.mu 
    def div(self):
        if self.n <2:
            return 0
        else:
            return(pow((self.m2/(self.n - 1)),0.5))
    def norm(self,x):
        if(x=='?'):
            return (x)
        else:
            return((x - self.lo) / (self.hi - self.lo + pow(10,-30)))
            
 
        
# obj=Num()
# obj.add(10)
# obj.add(23)
# obj.add(11)
# print(obj.mid())
# print(obj.div())
# print(obj.norm(200))
      
