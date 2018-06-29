def muliMatrix(m1,m2):
    res=[[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m2[0])):
        for j in range(len(m1)):
            for k in range(len(m2)):
                res[i][j]+=m1[i][k]*m2[k][j]
    return res
                
def matrixPower(m,p):
    res=[[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    for i in range(len(res)):#构建单位矩阵
        res[i][i]=1
    tmp=m
    while p>0:#快速幂
        if p&1!=0:
            res=muliMatrix(res,tmp)
        tmp=muliMatrix(tmp,tmp)
        p>>=1
    return res
    
def f3(n):#O(log N)
    if n<1:return 0
    if n==1 or n==2:return 1
    base=[[1,1],[1,0]]
    res=matrixPower(base,n-2)
    return res[0][0]+res[1][0]
    
print(f3(8))