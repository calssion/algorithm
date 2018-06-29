def isPost(arr:list, start:int, end:int)->bool:
    if start==end:return True
    less=-1
    more=end
    for i in range(start,end):
        #后序遍历根节点在最后，所以与根节点比划分左右子树
        if arr[end]>arr[i]:
            less=i
        else:
            more=i if more==end else more
    if less==-1 or more==end:
        return isPost(arr,start,end-1)
    if less!=more-1:return False
    return isPost(arr,start,less) and isPost(arr,more,end-1)
        
arr=[2,1,3,6,5,7,4]
print(isPost(arr,0,len(arr)-1))

class tree:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def pos2BST(posArr:list, start:int, end:int):
    if start>end:return None
    head=tree(posArr[end])
    less=-1
    more=end
    for i in range(start,end):
        if posArr[end]>posArr[i]:
            less=i
        else:
            more=i if more==end else more
    head.left=pos2BST(posArr,start,less)
    head.right=pos2BST(posArr,more,end-1)
    return head
    
head=pos2BST(arr,0,len(arr)-1)
def back(head):
    if head.left!=None:
        back(head.left)
    if head.right!=None:
        back(head.right)
    print(head.value,end=' ')
    
back(head)
print()