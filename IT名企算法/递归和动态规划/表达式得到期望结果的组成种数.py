def isValid(exp:str)->bool: #检查是否合法
    if len(exp)&1==0:return False
    for i in range(0,len(exp),2):
        if exp[i]!='1' and exp[i]!='0':
            return False
    for i in range(1,len(exp),2):
        if exp[i]!='&' and exp[i]!='|' and exp[i]!='^':
            return False
    return True
    
def num2(exp:str, desired:bool)->int: #动态规划求解
    if exp=='':print(exp);return 0
    if not isValid(exp):print(exp);return 0
    t=[[0 for _ in range(len(exp))] for _ in range(len(exp))]#true的种数
    f=[[0 for _ in range(len(exp))] for _ in range(len(exp))]#false的种数
    t[0][0]=0 if exp[0]=='0' else 1
    f[0][0]=0 if exp[0]=='1' else 1
    for i in range(2,len(exp),2):
        t[i][i]=0 if exp[0]=='0' else 1 #判断自身对或错
        f[i][i]=0 if exp[0]=='1' else 1
        for j in range(i-2,-1,-2):
            for k in range(j,i,2):#枚举exp[j..i]上的每种划分
                if exp[k+1]=='&':
                    #只有对&对才为对，所以t[j..i]=t[j..k]*t[k+2..i]
                    t[j][i]+=t[j][k]*t[k+2][i]
                    #其中1个为错则错
                    f[j][i]+=(f[j][k]+t[j][k])*f[k+2][i]+f[j][k]*t[k+2][i]
                elif exp[k+1]=='|':
                    #其中1个为对则对
                    t[j][i]+=(f[j][k]+t[j][k])*t[k+2][i]+t[j][k]*f[k+2][i]
                    #只有错|错才为错
                    f[j][i]+=f[j][k]*f[k+2][i]
                else:
                    #不同则为对
                    t[j][i]+=f[j][k]*t[k+2][i]+t[j][k]*f[k+2][i]
                    #相同则为错
                    f[j][i]+=f[j][k]*f[k+2][i]+t[j][k]*t[k+2][i]
    return t[0][len(t)-1] if desired else f[0][len(f)-1]
    
exp='1^0|0|1'
desired=False
print(num2(exp,desired))