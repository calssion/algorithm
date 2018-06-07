def TopK(arr:list):
    l=[]
    for i in arr:
        l.extend(i)
    l.sort(reverse=True)
    print(l)
    
arr=[[219,405,538,845,971],[148,558],[52,99,348,691]]
TopK(arr)