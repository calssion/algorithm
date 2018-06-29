def setBorderMap(m:list, right:list, down:list):#预处理
    r,c=len(m),len(m[0])
    if m[r-1][c-1]==1:
        right[r-1][c-1]=1
        down[r-1][c-1]=1
    for i in range(r-2,-1,-1):#右边界处理
        if m[i][c-1]==1:
            right[i][c-1]=1
            down[i][c-1]=down[i+1][c-1]+1
    for i in range(c-2,-1,-1):#下边界处理
        if m[r-1][i]==1:
            right[r-1][i]=right[r-1][i+1]+1
            down[r-1][i]=1
    for i in range(r-2,-1,-1):
        for j in range(c-2,-1,-1):
            if m[i][j]==1:
                right[i][j]=right[i][j+1]+1
                down[i][j]=down[i+1][j]+1
                
def hasSizeOfBorder(size:int, right:list, down:list)->bool:
    for i in range(len(right)-size+1):#能满足当前size的行
        for j in range(len(right[0])-size+1):#能满足当前size的列
            if right[i][j]>=size and down[i][j]>=size and \
                right[i+size-1][j]>=size and down[i][j+size-1]>=size:
                    return True
    return False
            
def getMaxSize(m:list)->int:
    right=[[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    down=[[0 for _ in range(len(m[0]))] for _ in range(len(m))]
    setBorderMap(m,right,down)
    for size in range(min(len(m),len(m[0])),0,-1):#先从最大规格找起
        if hasSizeOfBorder(size,right,down):
            return size
    
m=[
    [0,1,1,1,1],
    [0,1,0,0,1],
    [0,1,0,0,1],
    [0,1,1,1,1],
    [0,1,0,1,1]
]
print(getMaxSize(m))