def product1(arr:list)->list:#直接可除情况
    if arr==[] or len(arr)<2:return None
    count=0#数0的个数
    all=1
    for i in range(len(arr)):#全部乘起来
        if arr[i]!=0:
            all*=arr[i]
        else:
            count+=1
    res=[0]*len(arr)
    if count==0:#无0则直接除
        for i in range(len(arr)):
            res[i]=all//arr[i]
    if count==1:#只有1个0的情况，多个0则输出全为0
        for i in range(len(arr)):
            if arr[i]==0:
                res[i]=all
    return res
    
def product2(arr:list)->list:#不可直接除的情况
    if arr==[] or len(arr)<2:return None
    res=[0]*len(arr)
    res[0]=arr[0]
    for i in range(1,len(arr)):#左边累乘
        res[i]=res[i-1]*arr[i]
    tmp=1
    for i in range(len(arr)-1,0,-1):#右边累乘
        res[i]=res[i-1]*tmp
        tmp*=arr[i]
    res[0]=tmp
    return res
    
arr=[2,3,1,4]
print(product1(arr))
print(product2(arr))