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


def eg_sym():
    s=Sym()
    for x in [1,1,1,1,2,2,3]:
        s.add(x)
    mode,e=s.mid(),s.div()
    print(mode,e)
    return(e>1.37 and e<1.38 and mode==1)


def eg_data():
    n=0
    d=Data("/Users/Neelr/Desktop/ASE-24-Grp20/data/auto93.csv")
    i=1
    for row in d.rows:
        print(row)
      #  if(i%100==0):
       #     n=n+len(row)
      #  i+=1
        n+=1
    return(n==399)


def run_all():
    num_res=eg_num()
    sym_res=eg_sym()
    data_res=eg_data()

    print("Num Class:",num_res)
    print("Sym Class:",sym_res)
    print("Data Class:",data_res)

#run_all()

def run_tests(test_name):
    if(test_name=='all'):
        run_all()
    elif(test_name=='num'):
        print(eg_num())
    elif(test_name=='sym'):
        print(eg_sym())
    elif(test_name=='data'):
        print(eg_data())

#run_tests('all')

    


        







    

    