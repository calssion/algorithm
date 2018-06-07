class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.value=data
        
def morrisIn(head):#中序遍历
    if head==None:return
    cur1=head
    cur2=None
    while cur1!=None: #cur1作为当前子树根节点
        cur2=cur1.left #进入其左子树
        if cur2!=None: #找到其最右节点
            while cur2.right!=None and cur2.right!=cur1:
                cur2=cur2.right
            if cur2.right==None: #连接并进入以其他节点为根的子树
                cur2.right=cur1
                cur1=cur1.left
                continue
            else:
                cur2.right=None
        print(cur1.value,end=' ') 
        cur1=cur1.right #进入右子树
        
def morrisPre(head):#先序遍历
    if head==None:return
    cur1=head
    cur2=None
    while cur1!=None: #cur1作为当前子树根节点
        cur2=cur1.left #进入其左子树
        if cur2!=None: #找到其最右节点
            while cur2.right!=None and cur2.right!=cur1:
                cur2=cur2.right
            if cur2.right==None: #连接并进入以其他节点为根的子树
                cur2.right=cur1
                print(cur1.value,end=' ') 
                cur1=cur1.left
                continue
            else:
                cur2.right=None
        else:
            print(cur1.value,end=' ') 
        cur1=cur1.right #进入右子树
        
def reverseEdge(fro):#返回其最右节点的父节点
    pre=next=None
    while fro!=None:
        next=fro.right
        fro.right=pre
        pre=fro
        fro=next
    return pre
        
def printEdge(head): #打印右边界
    tail=reverseEdge(head)
    cur=tail
    while cur!=None:
        print(cur.value,end=' ')
        cur=cur.right
    #reverseEdge(tail)
        
def morrisPos(head):#后序遍历
    if head==None:return
    cur1=head
    cur2=None
    while cur1!=None: #cur1作为当前子树根节点
        cur2=cur1.left #进入其左子树
        if cur2!=None: #找到其最右节点
            while cur2.right!=None and cur2.right!=cur1:
                cur2=cur2.right
            if cur2.right==None: #连接并进入以其他节点为根的子树
                cur2.right=cur1
                cur1=cur1.left
                continue
            else:
                cur2.right=None
                printEdge(cur1.left) 
        cur1=cur1.right #进入右子树
    printEdge(head)
        
head=node(4)
left=node(2)
head.left=left
left.left=node(1)
left.right=node(3)
right=node(6)
head.right=right
right.left=node(5)
right.right=node(7)

morrisIn(head)
print()
morrisPre(head)
print()
morrisPos(head)
print()