def process(upper:int, col:int, left:int, right:int)->int:
    #left为左斜线影响,right为右斜线影响
    if col==upper:#成功,col为当前放置情况
        return 1
    mostright=res=0
    pos= upper&(~(col|left|right))#pos代表在3者影响下还有那些位置能放
    while pos!=0:
        mostright= pos&(~pos+1)#代表pos最右边的1在什么位置
        pos-=mostright#逐位尝试
        res+=process(upper,col|mostright,\
                (left|mostright)<<1,(right|mostright)>>1)
    return res
    
def num(n:int)->int:#位运算加速
    if n<1 or n>32:return 0
    upper= n==32 and -1 or (1<<n)-1 #upper为最终需要的状态
    return process(upper,0,0,0)
    
print(num(4))