class node:
    def __init__(self,data):
        self.value=data
        self.next=None
        
def mergeLR(left,right):
    next=None
    while left.next!=None:
        next=right.next
        right.next=left.next
        left.next=right
        left=right.next
        right=next
    left.next=right
    
def relocate(head):
    if head==None or head.next==None:return
    mid=head
    right=head.next
    while right.next!=None and right.next.next!=None: #找中点
        mid=mid.next
        right=right.next.next
    right=mid.next
    mid.next=None
    mergeLR(head,right)
    
head=p=node(0)
i=1
while i<10:
    q=node(i)
    p.next=q
    p=p.next
    i+=1
relocate(head)
while head!=None:
    print(head.value,end=' ')
    head=head.next