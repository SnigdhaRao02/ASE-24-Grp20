import math
import config

class Sym:
    def __init__(self,s="",n=0) -> None:
        self.at= n
        self.txt= s
        self.n=0    
        self.mode = "" #mean
        self.most = 0
        self.has={}
        self.mu = "N/A" # Since no mean of symbolic objects is calculated
        self.heaven=None # Havent defined it yet!!!
       
        #heaven to be added
    def add(self,x):
        if x!="?":
            self.n+=1
           
            if(x not in self.has.keys()):
                self.has[x]=1
            else:
                self.has[x]+=1
            if(self.has[x]>self.most):
                self.most,self.mode = self.has[x], x

    def mid(self):
        return self.mode
    def div(self):
        e=0
        for k in self.has:
            #print(self.has[k]/self.n)
            e=e-self.has[k]/self.n * math.log(self.has[k]/self.n,2)

        return e
    #Part of HW3
    def like(self,x,prior):
        #print(x)
        cons=(self.has.get(x,0)+(config.the.m)*prior)/(self.n+config.the.m)
        return(cons)
    
    # Add distance function -> dist
    def dist(self,x,y):
        if (x=="?" and y=="?"):
            return 1
        if (x==y):
            return 0
        else:
            return 1
    
    #hw7
    def bin(self,x):
        return x
        

    


  


    

        
    
        

      

