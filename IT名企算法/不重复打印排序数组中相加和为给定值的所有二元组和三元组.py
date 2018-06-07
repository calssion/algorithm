def pair(arr:list, k:int):
    if arr==[] or len(arr)<2:return
    left=0
    right=len(arr)-1
    while left<right:#二分法
        if arr[left]+arr[right]<k:
            left+=1
        elif arr[left]+arr[right]>k:
            right-=1
        else:
            if left==0 or arr[left-1]!=arr[left]:#排除重复值
                print(arr[left],arr[right])
            left+=1
            right-=1
            
def printRest(arr:list, f:int, l:int, r:int, k:int):#余下的作为二元组来算
    while l<r:
        if arr[l]+arr[r]<k:
            l+=1
        elif arr[l]+arr[r]>k:
            r-=1
        else:
            if l==f+1 or arr[l-1]!=arr[l]:
                print(arr[f],arr[l],arr[r])
            l+=1
            r-=1
            
def Triad(arr:list, k:int):
    if arr==[] or len(arr)<3:return
    for i in range(len(arr)-2):
        if i==0 or arr[i]!=arr[i-1]:#先选定一个
            printRest(arr,i,i+1,len(arr)-1,k-arr[i])
            
arr=[-8,-4,-3,0,1,2,4,5,8,9]
k=10
pair(arr,k)
Triad(arr,k)