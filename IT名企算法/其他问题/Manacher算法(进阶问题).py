def manstr(s:str)->str:
    s='#'+'#'.join(s)+'#'
    return s
    
def short(s:str)->str: #进阶问题
    if s is None or len(s)==0:return None
    s1=manstr(s)
    parr=[0]*len(s1)
    index=pr=maxend=-1
    for i in range(len(s1)):
        parr[i]= pr>i and min(parr[2*index-i],pr-i) or 1
        while i+parr[i]<len(s1) and i-parr[i]>-1:
            if s1[i+parr[i]]==s1[i-parr[i]]:
                parr[i]+=1
            else:
                break
        if i+parr[i]>pr:
            pr=i+parr[i]
            index=i
        if pr==len(s1):#到达串尾,要添加的即当前中心无法到达的左部分
            maxend=parr[i]
            break
    res=['']*(len(s)-maxend+1)
    for i in range(len(res)):#把左部分逆序赋予res
        res[len(res)-1-i]=s1[i*2+1]
    return ''.join(res)
    
print(short('abcd123321'))