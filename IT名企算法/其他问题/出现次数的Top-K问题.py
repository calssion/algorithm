import operator,collections
def topK(arr:str):
    d=collections.defaultdict(int)
    for i in arr:
        d[i]+=1
    j=1
    for i in sorted(d.items(),key=operator.itemgetter(1),reverse=True):
        print('Top',j,'is',i[0],' times:',i[1])
        j+=1
        
arr='aabc'
topK(arr)

#进阶问题
def add(arr:str, new:str)->str:
    return arr+new
    
arr=add(arr,'a')
arr=add(arr,'bb')
arr=add(arr,'dddddd')
print(arr)
topK(arr)