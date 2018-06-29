class tree:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
def pre(head):
    if head.left!=None:pre(head.left)
    print(head.value,end=' ')
    if head.right!=None:pre(head.right)
        
def pos(head,dist):
    if head==None:dist[0]=0;return 0
    lmax=pos(head.left,dist)
    ll=dist[0]
    rmax=pos(head.right,dist)
    rr=dist[0]
    cur=ll+rr+1
    dist[0]=max(ll,rr)+1
    return max(max(lmax,rmax),cur)
        
head=tree(1)
left=tree(2)
head.left=left
left.left=tree(3)
left.right=tree(4)
right=tree(5)
head.right=right
right.left=tree(6)
right.right=tree(7)
pre(head)
print()
print(pos(head,[0]))