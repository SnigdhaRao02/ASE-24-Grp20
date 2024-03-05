import math
import config
class Num:
    def __init__(self,s="",n=0) -> None:
        self.at= n
        self.txt= s
        self.n=0
        self.mu = 0 #mean
        self.m2 = 0
        self.lo,self.hi =1000000000000000, -1000000000000000
        self.heaven = 0 if s.endswith('-') else 1
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
        return round(self.mu,2) 
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
    
    #Part of HW3
    def like(self,x,_):
        mu,sd=self.mid(),(self.div()+pow(10,-30))
        #nom=pow(2.718,((pow(-0.5*(x-mu),2))/pow(sd,2)))
        nom=math.exp(-0.5 * (x - mu)**2 / sd**2)
        denom=(sd*2.5)+pow(10,-30)
        return(nom/denom)

    # Add distance function -> dist
    def dist(self,x,y):
        if (x=="?" and y=="?"):
            return 1
        #print("x,y",x,y)
        x,y= self.norm(x), self.norm(y)
        if x == "?":
            x = 1 if y < 0.5 else 0
        if y == "?":
            y = 1 if x < 0.5 else 0
        return abs(x-y)
    
    #hw7
    def bin(self,x):
        tmp=(self.hi-self.lo)/(config.the.bins-1)
        if self.hi==self.lo:
            return 1
        else:
            return math.floor(float(x)/tmp+0.5)*tmp
            
 
        
# obj=Num()
# obj.add(10)
# obj.add(23)
# obj.add(11)
# print(obj.mid())
# print(obj.div())
# print(obj.norm(200))
      

