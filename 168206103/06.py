start = "hit" 
end = "cog" 
ss=["hot","dot","dog","lot","log"]
res = []
processed=[]
dd=[]

def bb(processed,ss):
    aa(start,end,ss)
    print(processed)  
    
def aa(seq1,seq2,paths):
    ss.append(seq2)
    #print(len(ss))
    for i in range(len(ss)):
      #  print(seq1)
        for x in seq1:
            if x not in ss[i]:
                #print(ss[i])
                res.append(x)  
               # print(len(ss))
               # print(len(res))
        if len(res)==1:
            #print (ss[i])
           # print("\n")
            dd=ss[i]
            del res[:]
            seq1=ss[i]   
            processed.append(dd) 
        else:
            del res[:]
bb(processed,ss)
