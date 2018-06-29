def getnext(m:str)->list:
    if len(m)==1:
        return [-1]
    next=[0 for _ in range(len(m))]
    next[0]=-1
    pos=2 #从第三位开始，因为第二位前缀和后缀都为0
    cn=0
    while pos<len(next):
        if m[pos-1]==m[cn]: #直接匹配
            cn+=1
            next[pos]=cn
            pos+=1
        elif cn>0: #搜寻其他前缀
            cn=next[cn]
        else: #到第1位了
            next[pos]=0
            pos+=1
    return next

def getindex(s:str,m:str)->int:
    if s is None or m is None or len(m)<1 or len(s)<len(m):
        return -1
    si=mi=0
    next=getnext(m)
    while si<len(s) and mi<len(m):
        if s[si]==m[mi]: #匹配
            mi+=1
            si+=1
        elif next[mi]==-1: #头位
            si+=1
        else: #回退
            mi=next[mi]
    return mi==len(m) and si-mi or -1
    
s='bbabbabcabbabb'
m='abbabb'
print(getnext(m))
print(getindex(s,m))