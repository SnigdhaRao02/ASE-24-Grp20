from num import Num
from sym import Sym
from data import Data
from row import Row
import config
import re
import sys 
sys.path.append("../ASE-24-Grp20/")

import math
import random

def eg_num():
    e=Num()
    for _ in range(1,1000):
        e.add(random.normalvariate(10,2))
    mu,sd=e.mid(),e.div()
   # print(round(mu,3),round(sd,3))
    return(mu>10 and mu<10.1 and sd>2 and sd<2.05)


def eg_sym():
    s=Sym()
    for x in [1,1,1,1,2,2,3]:
        s.add(x)
    mode,e=s.mid(),s.div()
   # print(mode,e)
    return(e>1.37 and e<1.38 and mode==1)


def eg_data():
    n=0
    d=Data("/Users/challasaicharitha/gate/data/auto93.csv")
    i=1
    for row in d.rows:
       # print(row)
      #  if(i%100==0):
       #     n=n+len(row)
      #  i+=1
        n+=1
    return(n==399)






# hw 3 
def learn (data,row,my):
    my["n"]=my["n"]+1
    kl=row.cells[data.cols.klass.at]
    if(my["n"]>10):
        my["tries"]=my["tries"]+1
        if(kl==row.likes(my["datas"])[0]):
            my["acc"]+=1
    if(kl not in my["datas"]):
        my["datas"][kl]= Data(data.cols.names)
    my["datas"][kl].add(row.cells)


def eg_bayes():
    wme={
        "acc":0,
        "datas":{},
        "tries":0,
        "n":0
    }
    llearn = lambda data, t: learn(data, t, wme)
    
    Data("/Users/challasaicharitha/Desktop/ASE-24-Grp20/data/diabetes.csv",llearn)

    # for data in d.rows:
    #     data=Row(data)
    #     learn(d,data,wme)
    
    print("Accuracy: ",wme["acc"]/(wme["tries"]))
    return(wme["acc"]/(wme["tries"])>0.72)


def eg_km():
    
    for k in [0.001,1,2,3]:
        for m in [0.001,1,2,3]:
            config.the.k=k
            config.the.m=m 
            wme={
            "acc":0,
            "datas":{},
            "tries":0,
            "n":0
            }
            llearn = lambda data, t: learn(data, t, wme)
            Data("/Users/challasaicharitha/Desktop/ASE-24-Grp20/data/soybean.csv",llearn)
            print(wme["acc"]/(wme["tries"])," ",k," ",m)
    
def eg_gate20():
    print("best,mid")
    for i  in range(1,21):
        d= Data("C:/Users/tarje/Desktop/diabetes.csv")
        stats,bests=d.gate(4,16,0.5)
        stat, best= stats[-1], bests[-1]
        print(i," ",best.distance2heaven(d)," ", stat.distance2heaven(d))

print(eg_gate20())




def run_all():
    num_res=eg_num()
    sym_res=eg_sym()
    data_res=eg_data()
    if(num_res+sym_res+data_res==3):
       print("All three test cases passed!")
    

    
    bayes= eg_bayes()
    # km= eg_km()

    print("Num Class:",num_res)
    print("Sym Class:",sym_res)
    print("Data Class:",data_res)

    #Part of HW3
    print("Bayes: ",bayes)
    print("CHANGING K AND M VALUES: ")
    eg_km()

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
    
    
# run_tests('all')

    

        


        

    


        







    

    