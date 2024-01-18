from num import Num
from sym import Sym
from data import Data

import math
import random

def eg_num():
    e=Num()
    for _ in range(1,1000):
        e.add(random.normalvariate(10,2))
    mu,sd=e.mid(),e.div()
    print(round(mu,3),round(sd,3))
    return(mu>10 and mu<10.1 and sd>2 and sd<2.05)
print(eg_num())

def eg_sym():
    s=Sym()
    for x in [1,1,1,1,2,2,3]:
        s.add(x)
    mode,e=s.mid(),s.div()
    print(mode,e)
    return(e>1.37 and e<1.38 and mode==1)
print(eg_sym())

def eg_data():
    n=0
    d=Data("/Users/challasaicharitha/gate/data/auto93.csv")
    i=1
    for row in d.rows:
        print(row)
      #  if(i%100==0):
       #     n=n+len(row)
      #  i+=1
        n+=1
    return(n==399)
print(eg_data())
        







    

    