from num import Num
from sym import Sym
from data import Data
from row import Row
from range import Range
from rules import Rules
import config
import config2
import re
import sys 
from stats import egSlurp
import math
from datetime import datetime

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
    d=Data("C:/Users/tarje/Desktop/auto93.csv")
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
    ans=[[],[],[],[],[],[]]
    for i  in range(1,21):
        d= Data("C:/Users/tarje/Desktop/auto93.csv")
        stats,bests=d.gate(4,16,0.5,ans)
        stat, best= stats[-1], bests[-1]
      
        print(i," ",round(best.distance2heaven(d),2)," ", round(stat.distance2heaven(d),2))
    return ans

def test_distance2heaven():
    d= Data("C:/Users/tarje/Desktop/auto93.csv")
    ex = Row(t=[8,400,230,73,1,4278,9.5,20])
    res=ex.distance2heaven(d)
    return round(res,2) >= 0.8 or round(res,2) < 0.83

def test_gate():
    d= Data("C:/Users/tarje/Desktop/auto93.csv")
    budget0,budget,some=4,16,0.5
    stats,bests=d.gate(budget0,budget,some)
    for ele in stats:
        print(ele.cells)
    stat, best= stats[-1], bests[-1]
   # print(stat.cells,best.cells)
    print(1," ",best.distance2heaven(d)," ", stat.distance2heaven(d))
    if stats and bests:
        return True
    else:
        return('!!!!!!!!!!!!!!')

# Testing out how data is stored in the data object
def test_data():
    d = Data("C:/Users/tarje/Desktop/auto93.csv")
    for i in d.rows:
        print(i.cells)
    print("---------------------------------------")
    for j,k in d.cols.x.items():
        print(j, " ", k, " ", k.at, " ", k.txt, " ", k.n, " ", round(k.mu,2) if (not isinstance(k.mu,str)) else k.mu
        , " ", k.heaven)
    print("---------------------------------------")
    for j,k in d.cols.y.items():
        print(j, " ", k, " ", k.at, " ", k.txt, " ", k.n, " ", round(k.mu,2) if (not isinstance(k.mu,str)) else k.mu
        ," ", k.heaven)

def test_dist():
    d = Data("C:/Users/tarje/Desktop/auto93.csv")
    r1= d.rows[1]
    print(r1.cells)
    r2=d.rows[2]
    print(r2.cells)
    distance= r1.dist(r2,d)
    print(distance)

def test_neighbors():
    d = Data("C:/Users/tarje/Desktop/auto93.csv")
    r1=d.rows[1]
    print(r1.cells)
    rows= r1.neighbors(d)
    for i in rows:
        print(i.cells)

def eg_dist():
    d = Data("C:/Users/tarje/Desktop/auto93.csv")
    r1=d.rows[1]
    rows=r1.neighbors(d)
    for i in range(0,len(rows)):
        if((i+1)%30==0 or i==0):
            print(rows[i].cells, round(rows[i].dist(r1,d),2))

# test_data()
# test_dist()
# test_neighbors()
# eg_dist()
# Add eg_dist (Lua code below)
# function eg.dist(   d,rows,r1)
#   d  = DATA.new("../data/auto93.csv")
#   r1   = d.rows[1]
#   rows = r1:neighbors(d)
#   for i, row in pairs(rows) do
#     if i%30 ==0 then print(l.o(row.cells), l.rnd(row:dist(r1,d))) end end end

#print(eg_bayes())
#print(eg_km())

#print(eg_num())
#print("d2h: ",test_distance2heaven())
#print(test_gate())
# ans=eg_gate20()
# for i in ans:
#     for j in i:
#         print(j)
#         print()

#far test case
def eg_far():
    d = Data("C:/Users/tarje/Desktop/auto93.csv")
    a,b,C,evals=d.farapart(d.rows,True)
    print('--------------')
    print('far1: ', a.cells)
    print('far2: ', b.cells)
    print('distance= ',round(C,2))

# eg_far()
def eg_half():
    d = Data("C:/Users/tarje/Desktop/auto93.csv")
    lefts,rights,left,right,C,cut,evals=d.half(d.rows,True)
    print('-------------')
    print(len(lefts),len(rights),left.cells,right.cells,C,cut)

# eg_half()


def eg_tree():
    t,evals=Data("C:/Users/tarje/Desktop/auto93.csv").tree(True)
    t.show()
    
    print(f"evals: {evals}")
    print('-------------')
# eg_tree()

def eg_branch():
    d=Data("C:/Users/tarje/Desktop/auto93.csv")
    best,rest,evals=d.branch()
    print("Optimization Output")
    print("Single Descent Output")
    print(best.mid().cells)
    print("Evals:",evals)
    print('-------------')
    

# eg_branch()

def doubletap():
    d=Data("C:/Users/tarje/Desktop/auto93.csv")
    best1,rest,evals1=d.branch(32)
    best2,_,evals2=best1.branch(4)
    print("Double Tap Output") 
    print("Best:",best2.mid().cells)
    print("Rest:",rest.mid().cells)
    print("Evals:", evals1+evals2)

# doubletap()

# HW06 Code:-
def eg_hw6():
    src= "C:/Users/tarje/Desktop/auto93.csv"
    repeats = 20
    d=Data(src)
    print("date: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("file: ",src[src.rfind("/")+1:])
    print("repeats: ", repeats)
    print("seed: ", config.the.seed)
    print("rows: ", len(d.rows)-1)
    print("cols: ",len(d.cols.x) + len(d.cols.y) + 1 )
    print("names: ", d.rows[0].cells," D2h-")
    print("mid:   ", list(d.mid().cells.values())[1:],round(d.mid().distance2heaven(d),2))
    print("div: ", list(d.div().cells.values())[1:], round(d.div().distance2heaven(d),2))
    print("#")
    ans=[[],[],[],[],[],[]]
    for i in range(0,repeats):
        stats,bests=d.gate(4,5,0.5,ans)
        print("smo9 ",bests[-1].cells, round(bests[-1].distance2heaven(d),2))
    print("#")
    all_rows=d.rows[1:] # Removing the name columns
    # print(all_rows[0].cells)
    for i in range(0,repeats):
        any50= random.sample(all_rows,50)
        any50.sort(key=lambda a: a.distance2heaven(d))
        print("any50: ",any50[0].cells, round(any50[0].distance2heaven(d),2))
    print("#")
    all_rows.sort(key=lambda a: a.distance2heaven(d))
    print("100% ",all_rows[0].cells, round(all_rows[0].distance2heaven(d),2))

def sd(list):
    mean = sum(list) / len(list) 
    variance = sum([((x - mean) ** 2) for x in list]) / len(list) 
    res = variance ** 0.5
    return res

def eg_hw6_stats():
    random.seed(config.the.seed)
    src= "C:/Users/tarje/Desktop/auto93.csv"
    repeats = 20
    d=Data(src)
    print("date: ", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("file: ",src[src.rfind("/")+1:])
    print("repeats: ", repeats)
    print("seed: ", config.the.seed)
    print("rows: ", len(d.rows)-1)
    print("cols: ",len(d.cols.x) + len(d.cols.y) + 1 )
    all_rows=d.rows[1:] # Removing the name columns
    all_rows.sort(key=lambda a: a.distance2heaven(d))
    all_d2h=[]
    ans=[[],[],[],[],[],[]]
    for i in all_rows:
        all_d2h.append(i.distance2heaven(d))
    print("best: ",round(all_rows[0].distance2heaven(d),2))
    print("tiny: ",round(0.35*sd(all_d2h),2))
    file= open("stats.txt","w").close()
    file = open("stats.txt","a")

    print("#base", end=" ")
    file.write("base ")
    for i in all_d2h:
        file.write(str(round(i,2)) + " ")
    file.write("\n")

    print("#bonr9", end=" ")
    file.write("bonr9 ")
    for i in range(0,repeats):
        stats,bests=d.gate(4,5,0.5,ans)
        file.write(str(round(bests[-1].distance2heaven(d),2)) + " ")
    file.write("\n")

    print("#rand9", end=" ")
    file.write("rand9 ")
    for i in range(0,repeats):
        rand9= random.sample(all_rows,9)
        rand9.sort(key=lambda a: a.distance2heaven(d))
        file.write(str(round(rand9[0].distance2heaven(d),2)) + " ")
    file.write("\n")

    print("#bonr15", end=" ")
    file.write("bonr15 ")
    for i in range(0,repeats):
        stats,bests=d.gate(4,11,0.5,ans)
        # print("bonr9 ",bests[-1].cells, round(bests[-1].distance2heaven(d),2))
        file.write(str(round(bests[-1].distance2heaven(d),2)) + " ")
    file.write("\n")

    print("#rand15", end=" ")
    file.write("rand15 ")
    for i in range(0,repeats):
        rand15= random.sample(all_rows,15)
        rand15.sort(key=lambda a: a.distance2heaven(d))
        # print("any50: ",rand15[0].cells, round(rand15[0].distance2heaven(d),2))
        file.write(str(round(rand15[0].distance2heaven(d),2)) + " ")
    file.write("\n")

    print("#bonr20", end=" ")
    file.write("bonr20 ")
    for i in range(0,repeats):
        stats,bests=d.gate(4,16,0.5,ans)
        # print("bonr20 ",bests[-1].cells, round(bests[-1].distance2heaven(d),2))
        file.write(str(round(bests[-1].distance2heaven(d),2)) + " ")
    file.write("\n")

    print("#rand20", end=" ")
    file.write("rand20 ")
    for i in range(0,repeats):
        rand20= random.sample(all_rows,20)
        rand20.sort(key=lambda a: a.distance2heaven(d))
        # print("any50: ",rand20[0].cells, round(rand20[0].distance2heaven(d),2))
        file.write(str(round(rand20[0].distance2heaven(d),2)) + " ")
    file.write("\n")

    print("#rand358", end=" ")
    file.write("rand358 ")
    for i in range(0,repeats):
        rand358= random.sample(all_rows,358)
        rand358.sort(key=lambda a: a.distance2heaven(d))
        # print("any358: ",rand358[0].cells, round(rand358[0].distance2heaven(d),2))
        file.write(str(round(rand358[0].distance2heaven(d),2)) + " ")
    file.write("\n")
    file.close()
    #egSlurp()
# HW06 code end

# HW07 Code:-

def _ranges(cols, rowss):
    t=[]
    for _, col in cols.items():
        for range in _ranges1(col,rowss):
            t.append(range)
    return t

def _ranges1(col, rowss):
    out,nrows = {},0
    #print("top top", rowss)
    for y, rows in rowss.items():  
        #print("top rows",[x.cells for x in rows]) 
        #print('----------')
        #print(all(isinstance(x, (int, float)) for x in [1,"clfn",3]))
        nrows = nrows + len(rows)
        #print("rrrr",rows[:-1])
        for row in rows:
            #if all(isinstance(x, (int, float)) for x in row.cells):
            # print("row--",row.cells)
            x = row.cells[col.at]
           # print("x:---",x)
            if not x == "?":
                bin = col.bin(x)
            #print("bin:",bin)
                if bin not in out:
                    out[bin] =Range(col.at, col.txt, x)
                out[bin].add(x,y)
    out_list=[]
    for _,u in out.items():
        out_list.append(u)
        # print(u)
    out_list.sort(key=lambda x: x.x["lo"])
    # table.sort(out, function(a,b) return a.x.lo < b.x.lo end)
    return (isinstance(col,Sym) and col.has) and out_list or _mergeds(out_list, nrows/config2.the.bins)
    # return  col.has and out or _mergeds(out, nrows/config2.the.bins)

def _mergeds(ranges,tooFew):
    i,t=0,[]
    #print("ranges--", ranges)
    while i < len(ranges):
        a=ranges[i]
        if i<len(ranges)-1:
            both=a.merged(ranges[i+1],tooFew)
            if both:
                a=both
                i+=1
        t.append(a)
        i+=1
    if len(t)<len(ranges):
        return _mergeds(t,tooFew)
    for i in range(1,len(t)):
        t[i].x["lo"]=t[i-1].x["hi"]
    t[0].x["lo"]= -math.inf
    t[-1].x["hi"]= math.inf
    return t



def eg_hw7_bins():
    random.seed(config.the.seed)
    src= "D:/AssignmentNotes/NCSU Semester 1/Software Engineering/project 3/ASE-24-Grp20/data/auto93.csv"
    d=Data(src)
    branch=d.branch()
    # print("branch : ", len(branch), " rows")
    # for i in range(0,len(branch)-1):
    #     print(i, " : ", len(branch[i].rows))
    # print("Best rows (branch[0]) ie LIKE:", len(branch[0].rows))
    # print("Rest rows (branch[1]) ie HATE:", len(branch[1].rows))

    LIKE = branch[0].rows[1:] # Removing the row which has the column names
    HATE = random.sample(branch[1].rows[1:], 3*len(LIKE))# choosing 3 times as many rest as there are best
    
    # print("Count of LIKE ", len(LIKE))
    # print("Count of HATE ", len(HATE)) 
    # r= Range(0, "Cldrs", 0)
    # r.add(6,"LIKE")
    # r.add(-6,"HATE")
    # print(r.show())

    def score(range):
        return range.score("LIKE", len(LIKE), len(HATE))
    
    t=[]
    # print("cols--",d.cols.x.items())
    print("OUTPUT1:-------")
    for _, col in d.cols.x.items():
       print("")
       for v in _ranges1(col, {"LIKE" : LIKE, "HATE" :HATE}):
            print( {"at": v.at, "scored": v.scored, "txt": v.txt, "x": v.x, "y":v.y})
            t.append(v)
    
    maxx=score(t[0])

    def l_slice(t,go,stop,inc=None):
        if go and go<0:
            go+=len(t)
        if stop and stop<0:
            stop+=len(t)
        u=[]
        if stop > len(t):
            stop=len(t)
        for j in range(go-1, stop, (inc or 1)):
            u.append(t[j])
        return u
    print("OUTPUT2:-------")
    print("#scores: ")
    for v in l_slice(t,1,config.the.Beam):
        if score(v)>maxx*0.1:
            print(round(score(v),2), "\t", {"at": v.at, "scored": v.scored, "txt": v.txt, "x": v.x, "y":v.y})
    print("Count of LIKE ", len(LIKE))
    print("Count of HATE ", len(HATE)) 

        

# eg_hw7_bins()
# HW8 - Rules
def eg_rules():
    print("Building rules...")
    random.seed(config2.the.seed)
   # src= "D:/AssignmentNotes/NCSU Semester 1/Software Engineering/project 3/ASE-24-Grp20/data/auto93.csv"
    src="/Users/challasaicharitha/Desktop/ASE-24-Grp20/data/auto93.csv"
    d=Data(src)
    best0, rest, evals1 = d.branch(config2.the.d)
    best, _, evals2 = best0.branch(config2.the.D)
    # print(evals1 + evals2 + config2.the.D - 1) What is this number mean??

    LIKE = best.rows[1:] # Removing the row which has the column names
    HATE = random.sample(rest.rows[1:], 3*len(LIKE))# choosing 3 times as many rest as there are best
    rowss={"LIKE": LIKE, "HATE":HATE}
    print(len(_ranges(d.cols.x, rowss)))
    
    rules = Rules((_ranges(d.cols.x, rowss)), goal="LIKE", rowss=rowss)
    print("test rules", rules.sorted)
    for i,rule in enumerate(rules.sorted):
        print("test rule", rule)
        result=d.clone(rule.selects(rest.rows[1:]))
        print("result", result)
        if(len(result.rows[1:])>0):
            result.rows[1:].sort(key=lambda x: x.distance2heaven(d))
            print(rule.show())
            #print(round(rule.scored),round(result.mid().distance2heaven(d)))
            print(round(rule.scored),round(result.mid().distance2heaven(d),round(result.rows[1].distance2heaven(d))))
            #print(result.mid().cells,"  ",rule.show())
            

        


    

eg_rules()


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

    

        


        

    


        







    

    