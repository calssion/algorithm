def nextmin(arr,start):#下一个坡度的起点
    for i in range(start,len(arr)-1):
        if arr[i]<arr[i+1]:
            return i
    return len(arr)-1
    
def rightCands(arr,left,right):
    base=1
    cands=1
    for i in range(right-1,left-1,-1):
        if arr[i]==arr[i-1]:
            cands+=base
        else:
            base+=1
            cands+=base
    return cands,base
    
def candy1(arr):
    if arr==[] or len(arr)==0:return 0
    index=nextmin(arr,0)
    res,data=rightCands(arr,0,index)
    index+=1
    lbase=1
    next=0
    same=1
    while index!=len(arr):
        if arr[index]>arr[index-1]:#上坡
            lbase+=1
            res+=lbase
            same=1
            index+=1
        elif arr[index]<arr[index-1]:#下坡
            next=nextmin(arr,index-1)#下到多远
            data0,data1=rightCands(arr,index-1,next)
            next+=1
            if data1<=lbase:
                res+=data0-data1
            else:
                res+=-lbase*same+data0-data1+data1*same
            lbase=1
            index=next
            same=1
        else:#相同坡度
            res+=lbase
            same+=1
            index+=1
    return res

print(candy1([1,2,2]))