def getlen(num:int)->int: #获取数位
    l=0
    while num!=0:
        l+=1
        num//=10
    return l
    
def power10(base:int)->int: #求10的base次方
    return 10**base
    
def fun(num:int)->int:
    if num<1:return 0
    l=getlen(num)
    if l==1:return 1 #只有一位
    tmp=power10(l-1) #对应最高10次方数
    first=num//tmp #最高位
    fnum=num%tmp+1 if first==1 else tmp #最高位是1还是大于1
    #最高位为1，=除去最高位剩下的数+1；否则为最高位上1的数量
    other=first*(l-1)*(tmp//10) 
    #其他位=最高位数字*除去最高位剩下的位数*某一位固定为1情况数
    return fnum+other+fun(num%tmp)
    
print(fun(99))