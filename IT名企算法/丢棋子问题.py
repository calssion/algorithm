def log2n(n:int)->int:
    res=-1
    while n!=0:
        res+=1
        n>>=1
    return res
#转换为K个棋子可以扔M次最多解决多少层楼
def process(nlevel:int, kchess:int)->int:
    if nlevel<1 or kchess<1:return 0
    bstimes=log2n(nlevel)+1
    if kchess>=bstimes:return bstimes
    dp=[0 for _ in range(kchess)]
    res=0
    while True:
        res+=1
        previous=0
        for i in range(0,kchess):
            tmp=dp[i]
            dp[i]=dp[i]+previous+1
            previous=tmp
            if dp[i]>=nlevel:
                return res
    
print(process(105,2))