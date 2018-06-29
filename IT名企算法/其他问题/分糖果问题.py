def nextmin(arr,start):#下一个坡度的起点
    for i in range(start,len(arr)-1):
        if arr[i]<=arr[i+1]:
            return i
    return len(arr)-1
    
def rightCands(arr,left,right):
    n=right-left+1
    return n+n*(n-1)//2
    
def candy1(arr):#原问题
    if arr==[] or len(arr)==0:return 0
    index=nextmin(arr,0)
    res=rightCands(arr,0,index)
    index+=1
    lbase=1
    next=0
    rcands=0
    rbase=0
    while index!=len(arr):
        if arr[index]>arr[index-1]:#上坡
            lbase+=1
            res+=lbase
            index+=1
        elif arr[index]<arr[index-1]:#下坡
            next=nextmin(arr,index-1)#下到多远
            rcands=rightCands(arr,index-1,next)
            next+=1
            rbase=next-index+1
            res+=rcands+(-lbase if rbase>lbase else -rbase)#比较那个坡度大
            lbase=1
            index=next
        else:#相同坡度
            res+=1
            lbase=1
            index+=1
    return res

print(candy1([1,2,2]))