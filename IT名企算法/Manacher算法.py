def manstr(s:str)->str:
    s='#'+'#'.join(s)+'#'
    return s
    
def maxlen(s:str)->int:
    if s is None or len(s)==0:return 0
    s=manstr(s)
    index=pr=-1
    maxn=-0xfffff
    parr=[0]*len(s)
    for i in range(len(s)):
        parr[i]= pr>i and min(parr[2*index-i],pr-i) or 1
        while i+parr[i]<len(s) and i-parr[i]>-1:
            if s[i+parr[i]]==s[i-parr[i]]: #重叠边界能否再扩
                parr[i]+=1
            else:
                break
        if i+parr[i]>pr: #更新最右边界
            pr=i+parr[i]
            index=i #对应中心
        maxn=max(maxn,parr[i])
    return maxn-1
    
print(maxlen('abcd123321'))