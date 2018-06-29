def fun(n:int)->int:
    a,b=1,2
    if n==1:return a
    elif n==2:return b
    
    for i in range(2,n):
        a,b=b,a+b
    return b
    
print(fun(3))