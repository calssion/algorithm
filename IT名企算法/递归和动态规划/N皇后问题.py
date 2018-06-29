def isvalid(record:list, i:int, j:int)->bool:#record保存每一行放第几列
    for k in range(i):#遍历已放好的位置
        if j==record[k] or abs(record[k]-j)==abs(i-k):#同列或同对角
            return False
    return True
    
def process(i:int, record:list, n:int)->int:
    if i==n:#成功
        return 1
    res=0
    for j in range(n):#枚举每一列
        if isvalid(record,i,j):
            record[i]=j
            res+=process(i+1,record,n)#下一行
    return res
    
def num(n:int)->int:
    if n<1:return 0
    record=[0]*n
    return process(0,record,n)
    
print(num(4))